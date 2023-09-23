import argparse
import asyncio
import colorama
import concurrent
import git
import glob
import os
import psutil
import pyprctl
import random
import re
import subprocess
import sys
import threading
from collections import defaultdict
from colorama import Fore, Style
from contextlib import asynccontextmanager
from pynpm import NPMPackage
from resemble.monkeys import monkeys, no_chaos_monkeys
from typing import Any, AsyncIterator, Iterable, Optional
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer


def info(message: str):
    if sys.stdout.isatty():
        print(
            Fore.GREEN + Style.BRIGHT + message + Style.RESET_ALL,
            file=sys.stdout,
        )
    else:
        print(message, file=sys.stdout)


def warn(message: str):
    if sys.stdout.isatty():
        print(
            Fore.YELLOW + Style.BRIGHT + message + Style.RESET_ALL,
            file=sys.stdout,
        )
    else:
        print(message, file=sys.stdout)


def fail(message: str):
    if sys.stderr.isatty():
        print(
            Fore.RED + Style.BRIGHT + message + Style.RESET_ALL,
            file=sys.stderr,
        )
    else:
        print(message, file=sys.stderr)
    sys.exit(1)


@asynccontextmanager
async def watch(
    application: str, paths: list[str]
) -> AsyncIterator[asyncio.Task[FileSystemEvent]]:
    """Helper for watching the provided paths on file system. Implemented
    as a context manager to ensure proper cleanup of the watches."""
    loop = asyncio.get_running_loop()

    class EventHandler(FileSystemEventHandler):

        def __init__(self, events: asyncio.Queue[FileSystemEvent]):
            self._events = events

        def on_modified(self, event):
            loop.call_soon_threadsafe(lambda: self._events.put_nowait(event))

    events: asyncio.Queue[FileSystemEvent] = asyncio.Queue()

    handler = EventHandler(events)

    observer: Optional[Observer] = None

    # It's possible that the application or other watch paths may get
    # deleted and then (re)created by a build system so rather than
    # fail if we can't find them we'll retry but print out a warning
    # after so many retries.
    #
    # We've picked 10 based on how long we've noticed some builds
    # taking.
    def warn_every_n_retries(retries: int, message: str):
        if retries != 0 and retries % 10 == 0:
            warn(message)

    retries = 0
    while True:
        # Construct a new observer everytime to avoid re-adding the
        # same path and raising an error.
        observer = Observer()

        try:
            if not os.path.isfile(application):
                warn_every_n_retries(
                    retries,
                    f"Missing application at '{application}' "
                    "(is it being rebuilt?)",
                )
                raise RuntimeError('Retry')

            observer.schedule(handler, path=application, recursive=False)

            # We want to (re)determine the paths to watch _every_ time
            # to find any new subdirectories added by the developer
            # which they surely expect we will properly watch as well.
            for unglobed_path in paths:
                has_globbed_paths = False
                for path in glob.iglob(unglobed_path, recursive=True):
                    has_globbed_paths = True

                    if not os.access(path, os.R_OK):
                        fail('Expecting path passed to --watch to be readable')

                    observer.schedule(handler, path=path, recursive=False)

                if not has_globbed_paths:
                    warn(f"'{unglobed_path}' did not match any files")

            observer.start()
            break
        except:
            # NOTE: we capture all exceptions here because
            # 'observer.schedule()' may raise if a file that we had
            # globbed gets removed before calling it (e.g., by a build
            # system) and we just want to retry since the build system
            # should be completing and not removing files out from
            # underneath us all the time.
            retries += 1
            await asyncio.sleep(0.5)
            continue

    # Ok, should have a valid observer now!
    assert observer is not None

    events_get = asyncio.create_task(events.get())

    try:
        yield events_get
    finally:
        events_get.cancel()
        observer.stop()
        observer.join()


async def terminate(process: subprocess.Popen | asyncio.subprocess.Process):
    """Helper for terminating a process and all of its descendants.

    This is non-trivial to do as processes may have double forked and
    are no longer part of the process tree, but there are a handful of
    different mechanisms that we document extensively within the
    implementation for how we try and kill all possible descedants of
    a process.
    """
    while True:
        # Try and get all the processes descendants first, before we
        # try and terminate it and lose the process tree.
        descendants = set()

        # (1) Add processes with same PGID as 'process'.
        #
        # This gets all processes that 'process' created that did not
        # create a new process group, even if they double forked and
        # are no longer direct descendants of 'process'.
        try:
            pgid = os.getpgid(process.pid)
        except ProcessLookupError:
            # Process might have already exited, e.g., because it
            # crashed, or we already killed it.
            #
            # Use the PID as PGID as they should be the same since
            # when the process was created it created a new process
            # group whose ID is the same as the PID.
            pgid = process.pid

        for p in psutil.process_iter():
            try:
                if os.getpgid(p.pid) == pgid:
                    descendants.add(p)
            except ProcessLookupError:
                # Process might have already exited, e.g., because it
                # crashed, or we already killed it.
                pass

        # (2) Add descendants of 'process'.
        #
        # This gets processes that might have changed their process
        # group but are still descendants of 'process'.
        try:
            for p in psutil.Process(process.pid).children(recursive=True):
                descendants.add(p)
        except psutil.NoSuchProcess:
            # Process 'process' might have already exited, e.g.,
            # because it crashed, or we already killed it.
            pass

        # Send SIGTERM to the process _but not_ the descendants to let
        # it try and clean up after itself first.
        #
        # Give it some time, but not too much time, before we try and
        # terminate everything.
        try:
            process.terminate()
            await asyncio.sleep(0.1)
        except ProcessLookupError:
            # Process might have already exited, e.g., because it
            # crashed, or we already killed it.
            pass

        # (3) Add _our_ descendants that have a different PGID.
        #
        # On Linux when we enable the subreaper so any processes that
        # both changed their process group and tried to double fork so
        # that they were no longer a descendant of 'process' should
        # now be a descendant of us however they will be in a
        # different process group than us.
        #
        # Note that while using the subreaper on Linux implies that
        # (3) subsumes (1), because the subreaper is best effort (as
        # in, we don't rely on having the requisite capabilities to
        # use the subreaper), we include them both.
        pgid = os.getpgid(os.getpid())

        for p in psutil.Process(os.getpid()).children(recursive=True):
            try:
                if os.getpgid(p.pid) != pgid:
                    descendants.add(p)
            except ProcessLookupError:
                # Process 'p' might have already exited, e.g., because
                # it crashed or we already killed it (but it actually
                # exited after it was determined one of our children).
                pass

        # Don't try and terminate ourselves! This can happen when we
        # try and terminate any processes that we were not able to put
        # into a separate process group.
        descendants = set(
            [
                descendant for descendant in descendants
                if descendant.pid != os.getpid()
            ]
        )

        if len(descendants) == 0:
            break

        for descendant in descendants:
            try:
                descendant.terminate()
            except psutil.NoSuchProcess:
                # Process might have already exited, e.g., because it
                # crashed, or we already killed it.
                pass

        _, alive = psutil.wait_procs(descendants, timeout=1)

        for descendant in alive:
            try:
                descendant.kill()
            except psutil.NoSuchProcess:
                # Process might have already exited, e.g., because
                # it crashed, or we already killed it.
                pass

        # Can wait forever here because a process can't ignore kill.
        psutil.wait_procs(alive)


@asynccontextmanager
async def run(application, *, launcher: Optional[str]):
    """Helper for running the application with an optional launcher."""
    process = await asyncio.create_subprocess_exec(
        application,
        # NOTE: starting a new sesssion will also put the
        # process into its own new process group. Each time we
        # restart the application we need to kill all
        # processes which are not in our process group as that
        # implies that they are processes that were created by
        # the application or one of its descendants.
        start_new_session=True,
    ) if launcher is None else await asyncio.create_subprocess_exec(
        launcher,
        application,
        # NOTE: see comment above on sessions.
        start_new_session=True,
    )
    try:
        yield process
    finally:
        await terminate(process)


def default_package_json() -> str:
    return os.path.join(os.getcwd(), "web/package.json")


default_local_envoy_port: int = 9991


def dot_rsm_directory() -> str:
    """Helper for determining the '.rsm' directory."""
    try:
        repo = git.Repo(search_parent_directories=True)
    except git.exc.InvalidGitRepositoryError:
        return os.path.join(os.getcwd(), '.rsm/dev')
    else:
        return os.path.join(repo.working_dir, '.rsm/dev')


def npm_install_and_start(package_json: str) -> subprocess.Popen:
    """Helper that effectively does 'npm install' and then 'npm start'."""
    if not os.path.isfile(package_json):
        fail(f"Expecting 'package.json' at '{package_json}'")
    elif not os.access(package_json, os.R_OK):
        fail(f"Expecting 'package.json' to readable")

    package = NPMPackage(package_json)

    # Wait for 'install' to complete so if it has any errors we don't
    # bother doing anything else yet.
    package.install()

    # Run 'start' with 'wait=False' so we can get back the process in
    # order to watch for it to terminate. Also this creates a pipe for
    # stdout/stderr which prevents npm/node from thinking it's writing
    # to a TTY and thus prevents it from clearing the terminal which
    # is a rather frustrating developer experience. If we are on a
    # TTY, however, we first set the environment variable
    # FORCE_COLOR=true so that we still get color output!
    #
    # See https://github.com/facebook/create-react-app/issues/2495 for
    # discussion on this "workaround" being the blessed approach.
    if sys.stdout.isatty():
        os.environ['FORCE_COLOR'] = 'true'

    # TODO(benh): the NPMPackage module starts the process in such a
    # way that it becomes the tty leader such that when it exits the
    # shell will display the prompt even though we are still
    # running. We likely need to just make the 'npm start' call
    # ourselves instead of using NPMPackage.
    package_start_process = package.start(wait=False)

    # TODO(benh): watch to see if process terminates!

    # NOTE: NPMPackage redirects stderr to stdout when passing
    # 'wait=False', so we only need to redirect stdout from the
    # process.
    def redirect():
        while True:
            line = package_start_process.stdout.readline()
            if not line:
                break
            sys.stdout.write(line.decode('utf-8'))

    # TODO(benh): do this via asyncio? Might not be possible because
    # 'package.start()' doesn't use 'asyncio.subprocess'?
    threading.Thread(target=redirect, daemon=True).start()

    return package_start_process


async def dev(args):
    """Implementation of the 'dev' subcommand."""
    application = os.path.abspath(args.application)

    if not os.path.isfile(application):
        fail(f"No application at '{application}'")
    elif not os.access(application, os.X_OK):
        fail(f"Expecting executable application at '{application}'")

    # If on Linux try and become a child subreaper so that we can
    # properly clean up all processes descendant from us!
    if sys.platform == 'linux':
        try:
            pyprctl.set_child_subreaper(True)
        except:
            warn(
                "Failed to become child subreaper, we'll do our "
                "best to ensure all created processes are terminated"
            )
            pass

    # TODO(benh): support both 'yarn' and 'npm' and distinguish via
    # extra command line options.
    npm = args.fullstack

    package_start_process: Optional[subprocess.Popen] = None

    if npm:
        package_start_process = npm_install_and_start(
            args.package_json or default_package_json()
        )

    # Set all the environment variables that
    # 'resemble.aio.Application' will be looking for.

    os.environ['RSM_DEV'] = 'true'

    if args.name is not None:
        os.environ['RSM_DEV_NAME'] = args.name
        os.environ['RSM_DOT_RSM_DIRECTORY'] = dot_rsm_directory()

    os.environ['RSM_DEV_LOCAL_ENVOY'] = 'true' if (
        args.local_envoy if args.local_envoy is not None else args.fullstack
    ) else 'false'

    os.environ['RSM_DEV_LOCAL_ENVOY_PORT'] = str(
        args.local_envoy_port or default_local_envoy_port
    )

    if not args.chaos:
        warn(
            '\n' + random.choice(no_chaos_monkeys) + '\n'
            'You Have Disabled Chaos Monkey! (see --chaos)\n'
            '\n'
            'Only You (And Chaos Monkey) Can Prevent Bugs!'
            '\n'
        )

    try:
        while True:
            if args.name is None:
                warn(
                    '\n'
                    'Starting an ANONYMOUS application; to reuse state '
                    'across application restarts use --name'
                    '\n'
                )

            async with watch(
                application, args.watch or []
            ) as file_system_event_task:
                # TODO(benh): catch just failure to create the subprocess
                # so that we can either try again or just listen for a
                # modified event and then try again.
                async with run(
                    application,
                    # TODO(benh): use executable in env var $PYTHON if it exists.
                    launcher='python' if args.python is not None else None,
                ) as process:
                    process_wait_task = asyncio.create_task(process.wait())

                    if args.chaos:
                        chaos_task = asyncio.create_task(
                            asyncio.sleep(random.randint(30, 60))
                        )

                    completed, pending = await asyncio.wait(
                        [file_system_event_task, process_wait_task] +
                        ([chaos_task] if args.chaos else []),
                        return_when=asyncio.FIRST_COMPLETED,
                    )

                    # Cancel chaos task regardless of what task
                    # completed first as we won't ever wait on it.
                    if args.chaos:
                        chaos_task.cancel()

                    task = completed.pop()

                    if task is process_wait_task:
                        warn(
                            '\n'
                            'Application exited unexpectedly '
                            '... waiting for modification'
                            '\n'
                        )
                        # NOTE: we'll wait for a file system event
                        # below to signal a modification!
                    elif args.chaos and task is chaos_task:
                        warn(
                            '\n'
                            'Chaos Monkey Is Restarting Your Application'
                            '\n' + random.choice(monkeys) + '\n'
                            '... disable via --no-chaos if you must'
                            '\n'
                            '\n'
                        )
                        continue

                    file_system_event: FileSystemEvent = await file_system_event_task

                    info('\n'
                         'Application modified; restarting ... '
                         '\n')
    except:
        if npm:
            assert package_start_process is not None
            await terminate(package_start_process)
        raise


# Type aliases to help better undersatnd types.
Subcommand = str
Config = str
Flag = str

# Regular expression patterns used for '.rc' file parsing.
#
# Pattern for subcommand, e.g., 'dev --some-flag and_args'.
SUBCOMMAND_PATTERN = r'^(\.\.\.|[A-Za-z0-9]+)[ ].+$'

# Pattern for subcommand:config, e.g., 'dev:foo --some-flag and_args'.
SUBCOMMAND_CONFIG_PATTERN = r'^(\.\.\.|[A-Za-z0-9]+):[A-Za-z0-9]+[ ].+$'

# String representing flags for "common" expansion.
COMMON_PATTERN = '...'


class RcArgumentParser:
    """A CLI argument/options/flags parser that knows how to expand
    arguments found in a '.rc', e.g, '.rsmrc'.

    Formatting expected in a '.rc' file:

    (1) Comments. Any line starting with a '#' is skipped. All text
        after a trailling '#' is also dropped.

    (2) "Common" flags, i.e., flags that are relevant for all
        subcommands, defined by the top-level parser, are
        distinguished via a line that starts with '...':

        # Always expanded.
        ... --more-flags=42 and_args here

    (3) Subcommand specific flags:

        # Always expanded when invoking subcommand.
        subcommand --more-flags=42 and_args here

    (4) Config flags expanded from '--config=foo' for both "common"
        and subcommands:

        # Only expanded if --config=foo.
        ...:foo --flag=42
        subcommand:foo --more-flags=42

    (5) Recursive configs are fully supported:

        dev:fullstack --fullstack

        dev:demo --config=fullstack

    (6) All lines are aggregated.

        dev:demo --config=fullstack  # The demo is "fullstack".
        dev:demo --name=demo         # Name of demo.
        dev:demo --python            # Uses Python.


    TODO(benh): move this into own file 'rc_argument_parser.py'
    if/once we need it for other CLI tools.
    """

    def __init__(
        self,
        *,
        filename: str,
        subcommands: list[str],
        file: Optional[str] = None,
        argv: Optional[list[str]] = None,
    ):
        self._parser = argparse.ArgumentParser()

        self._subparsers = self._parser.add_subparsers(
            dest='subcommand', required=True
        )

        self.subcommand_parsers: dict[str, argparse.ArgumentParser] = {}

        for subcommand in subcommands:
            self.subcommand_parsers[subcommand] = self._subparsers.add_parser(
                subcommand
            )

            # Ensure every subcommand has a '--config=' argument to
            # support configuration in '.rc' files.
            self.subcommand_parsers[subcommand].add_argument(
                '--config',
                action='append',
                help=f"\"configs\" to apply from a '{filename}' file, "
                f"e.g., 'rsm {subcommand} --config=foo' would add all flags "
                f"on lines in the '{filename}' that start with '{subcommand}:foo'",
            )

        self._argv = argv or sys.argv

        # Try to expand flags from a '.rc'
        #
        # NOTE: we must do this _before_ the rest of the arguments are
        # added because in order to properly expand flags for
        # subcommands we have to run the parser which will fail if we
        # are missing required arguments that are in fact not yet
        # expanded from the '.rc' file.
        dot_rc: Optional[str] = file or RcArgumentParser._find_dot_rc(filename)

        if dot_rc is not None:
            self._argv = RcArgumentParser._expand_dot_rc(
                filename,
                dot_rc,
                self._parser,
                subcommands,
                self._argv,
            )

    def parse_args(self):
        """Pass through to `argparse` with the expanded arguments."""
        return self._parser.parse_args(args=self._argv[1:])

    @staticmethod
    def _find_dot_rc(filename: str) -> Optional[str]:
        """Tries to find the '.rc' file in the current directory or, if in a
        git repository, in the top-level directory of the repository,
        and returns the path if found otherwise `None`."""
        dot_rc: Optional[str] = None

        dot_rc = os.path.join(os.getcwd(), filename)
        if not os.path.isfile(dot_rc):
            try:
                repo = git.Repo(search_parent_directories=True)
            except git.exc.InvalidGitRepositoryError:
                return None
            else:
                dot_rc = os.path.join(repo.working_dir, filename)
                if not os.path.isfile(dot_rc):
                    return None

        assert dot_rc is not None

        if not os.access(dot_rc, os.R_OK):
            fail(f"Found '{filename}' at {dot_rc} but it is not readble")

        return os.path.abspath(dot_rc)

    @staticmethod
    def _read_flags_from_dot_rc(
        filename: str,
        dot_rc: str,
        subcommands: Iterable[str],
    ) -> defaultdict[tuple[Subcommand, Optional[Config]], list[Flag]]:
        """Returns the flags that should be added to the command line, keyed by
        the subcommand and config for those flags, or the empty tuple if
        they should be applied to all command lines.
        """
        flags: defaultdict[tuple[Subcommand, Optional[Config]],
                           list[Flag]] = defaultdict(list)

        with open(dot_rc, 'r') as file:
            line_number = 0
            for line in file.readlines():
                line_number += 1
                line = line.strip()  # Remove leading and trailing whitespaces.

                # Remove any trailing comments.
                index = line.rfind('#')
                if index != -1:
                    line = line[:index]

                if line == '' or line.startswith('#'):
                    continue
                elif re.match(SUBCOMMAND_PATTERN, line):
                    parts = line.split()
                    assert len(parts) > 0
                    flags[(parts[0], None)].extend(parts[1:])
                elif re.match(SUBCOMMAND_CONFIG_PATTERN, line):
                    parts = line.split()
                    assert len(parts) > 0
                    subcommand, config = parts[0].split(':', 1)
                    assert subcommand is not None
                    if subcommand not in [COMMON_PATTERN, *subcommands]:
                        fail(
                            f"'{subcommand}' found at {dot_rc}:{line_number} "
                            "is not a valid subcommand (available subcommands: "
                            f"{', '.join(subcommands)})"
                        )

                    flags[(subcommand, config)].extend(parts[1:])
                else:
                    fail(
                        f"Failed to parse '{filename}' file at {dot_rc}:{line_number}"
                    )

        return flags

    @staticmethod
    def _expand_dot_rc(
        filename: str,
        dot_rc: str,
        parser: argparse.ArgumentParser,
        subcommands: Iterable[str],
        argv: list[str],
    ) -> list[str]:
        """Expand '.rc' file into `argv`."""
        flags = RcArgumentParser._read_flags_from_dot_rc(
            filename, dot_rc, subcommands
        )

        # Now add all "common" flags and parse to determine subcommand.
        common_flags = flags[(COMMON_PATTERN, None)]
        if len(common_flags) > 0:
            argv = argv[:1] + common_flags + argv[1:]

        # Parse command line but only looking for subcommands and
        # '--config=' flags.
        known_args, _ = parser.parse_known_args(args=argv[1:])

        # Expand flags for just '{subcommand}'.
        subcommand = known_args.subcommand

        # Subcommands are required.
        assert subcommand is not None

        subcommand_flags: list[Flag] = []

        # Now add '{subcommand}' specific flags.
        subcommand_flags = flags[(subcommand, None)]
        if len(subcommand_flags) > 0:
            argv.extend(subcommand_flags)

        # Now expand config flags.
        configs = known_args.config or []

        common_config_flags: dict[Config, list[Flag]] = {}
        subcommand_config_flags: dict[Config, list[Flag]] = {}

        while not all(
            (config in common_config_flags) and
            (config in subcommand_config_flags) for config in configs
        ):
            for config in configs:
                # In order for 'config' to be valid we must find
                # either '{COMMON_PATTERN}:{config}' or
                # '{subcommand}:{config}' in the '{filename}' file.
                expanded = (
                    config in common_config_flags and
                    config in subcommand_config_flags
                )

                # Expand '{COMMON_PATTERN}:{config}' flags, but prepend
                # those (after `argv[0]`, but before `argv[1]`).
                if config not in common_config_flags:
                    if (COMMON_PATTERN, config) in flags:
                        expanded = True
                        common_config_flags[config] = flags[
                            (COMMON_PATTERN, config)]
                        argv = argv[:1] + common_config_flags[config] + argv[1:]
                    else:
                        # Store the config so we know it was processed and
                        # we can halt the otherwise infinite while loop.
                        common_config_flags[config] = []

                # Expand '{subcommand}:{config}' flags.
                if config not in subcommand_config_flags:
                    if (subcommand, config) in flags:
                        expanded = True
                        subcommand_config_flags[config] = flags[
                            (subcommand, config)]
                        argv.extend(subcommand_config_flags[config])
                    else:
                        # Store the config so we know it was processed and
                        # we can halt the otherwise infinite while loop.
                        subcommand_config_flags[config] = []

                if not expanded:
                    fail(
                        f"--config={config} is invalid, no "
                        f"'{COMMON_PATTERN}:{config}' nor '{subcommand}:{config}' "
                        f"lines found in {dot_rc}"
                    )

            # Now re-parse the known args so we can see whether or not
            # expanding the last configs added any more configs that
            # we need to continue expanding.
            #
            # NOTE: we pass a copy of `argv` here so that we don't
            # mutate the original `argv` which we'll need to use for
            # our ultimate parsing, after we've expanded all of the
            # configs.
            known_args, _ = parser.parse_known_args(args=argv[1:])

            assert subcommand == known_args.subcommand
            configs = known_args.config

        if (
            len(common_flags) > 0 or len(subcommand_flags) > 0 or
            len(subcommand_config_flags) > 0
        ):
            warn(f"Expanded flags from '{filename}' located at {dot_rc}")
            if len(common_flags) > 0:
                warn(
                    f"    {' '.join(common_flags)} (from '{COMMON_PATTERN}' in '{filename}')"
                )

            if len(subcommand_flags) > 0:
                warn(
                    f"    {' '.join(subcommand_flags)} (from '{subcommand}' in '{filename}')"
                )

            for config, config_flags in common_config_flags.items():
                if len(config_flags) > 0:
                    warn(
                        f"    {' '.join(config_flags)} (from '{COMMON_PATTERN}:{config}' in '{filename}' via --config={config})"
                    )

            for config, config_flags in subcommand_config_flags.items():
                if len(config_flags) > 0:
                    warn(
                        f"    {' '.join(config_flags)} (from '{subcommand}:{config}' in '{filename}' via --config={config})"
                    )

        return argv


async def rsm():
    colorama.init()

    parser = RcArgumentParser(filename='.rsmrc', subcommands=['dev'])

    parser.subcommand_parsers['dev'].add_argument(
        '--name',
        type=str,
        help="name of instance; state will be persisted using this name in "
        f"'{dot_rsm_directory()}'",
    )

    parser.subcommand_parsers['dev'].add_argument(
        '--fullstack',
        action='store_true',
        help="also run 'npm start'",
    )

    parser.subcommand_parsers['dev'].add_argument(
        '--package-json',
        type=str,
        help=
        f"path to your 'package.json'; or we'll try '{default_package_json()}'",
    )

    parser.subcommand_parsers['dev'].add_argument(
        '--local-envoy',
        action='store_const',
        const=None,
        help='whether or not to bring up a local envoy; '
        'defaults to true if --fullstack',
    )

    parser.subcommand_parsers['dev'].add_argument(
        '--local-envoy-port',
        type=int,
        help=f'port for local envoy; defaults to {default_local_envoy_port}',
    )

    parser.subcommand_parsers['dev'].add_argument(
        '--python',
        action='store_true',
        help="whether or not to launch the application by "
        "passing it as an argument to 'python'",
    )

    parser.subcommand_parsers['dev'].add_argument(
        '--watch',
        action='append',
        help=
        'path to watch; multiple instances are allowed; globbing is supported',
    )

    parser.subcommand_parsers['dev'].add_argument(
        '--chaos',
        action=argparse.BooleanOptionalAction,
        default=True,
        help='whether or not to randomly induce failures',
    )

    parser.subcommand_parsers['dev'].add_argument(
        # TODO: consider argparse.FileType('e')
        'application',
        type=str,
        help='path to application to execute',
    )

    args = parser.parse_args()

    if args.subcommand == 'dev':
        await dev(args)
    else:
        parser.print_help()


# This is a separate function (rather than just being in `__main__`) so that we
# can refer to it as a `script` in our `pyproject.rsm.toml` file.
def main():
    try:
        asyncio.run(rsm())
    except KeyboardInterrupt:
        # Don't print an exception and stack trace if the user does a
        # Ctrl-C.
        pass


if __name__ == '__main__':
    main()
