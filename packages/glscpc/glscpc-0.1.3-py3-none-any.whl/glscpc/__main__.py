import logging
import shlex
import shutil
import traceback
from typing import Any, BinaryIO

import click
from click.exceptions import Exit

from glscpc import process_file

from ._version import __version__

VERBOSE_OPTIONS = [logging.WARNING, logging.INFO, logging.DEBUG]
# Default command: Take from stdin, use POSIX shell, format output as JSON1
DEFAULT_COMMAND = ["shellcheck", "-", "--shell=sh", "--format=json1"]
QTEAL = click.style("Q", fg="cyan") + click.style("teal", fg="bright_black")
LOGO = f"""
┏━╸╻  ┏━┓┏━╸┏━┓┏━╸  {QTEAL}
┃╺┓┃  ┗━┓┃  ┣━┛┃    {click.style('fixing systems, not people', fg='bright_black')}
┗━┛┗━╸┗━┛┗━╸╹  ┗━╸  v{__version__}
""".strip()
# Padding required to make sure click keeps the logo intact.
HELP = f"""
Check your .gitlab-ci.yml scripts with ShellCheck.

This project does not lint the rest of the files and assumes they are well-formed and valid.
Please use another checker for that purpose.

Any other arguments passed will be forwarded to shellcheck as additional arguments.
The full command is printed when DEBUG logging is enabled.

To pass arguments that conflict with glscpc, use -- to end the parsing of options for glscpc.
"""


def transform_return(e: Any) -> str:
    """
    Process the returned (or yielded) values from process_file into strings for output to user.
    """
    if isinstance(e, str):
        return e
    if isinstance(e, Exception):
        return "".join(traceback.format_exception_only(e))
    return repr(e)


@click.command(
    context_settings={
        # Help is still wrapped to terminal width, but ignore the 80 char default max.
        "max_content_width": 1000,
        # All unknown options are passed to shellcheck later
        "ignore_unknown_options": True,
    },
    # \b selectively disables all re-wrapping on the next paragraph, which makes the logo work.
    help="\b\n" + LOGO + "\n" + HELP,
)
@click.version_option(__version__)
@click.option(
    "-f",
    "--file",
    "files",
    type=click.File("rb"),
    multiple=True,
    help="Specify one or more .gitlab-ci.yml files.",
    default=[".gitlab-ci.yml"],
)
@click.option(
    "-v",
    "--verbose",
    count=True,
    type=click.IntRange(min=0, max=len(VERBOSE_OPTIONS) - 1),
    help="Increase logging verbosity on stderr (once for INFO, twice for DEBUG)",
)
@click.option(
    "--cmd",
    help="Overwrite the default shellcheck command. "
    "Must be specified as a single command that will be split into arguments via shlex.split. "
    "Take care to set the output format to json1.",
)
@click.argument("args", nargs=-1, type=click.UNPROCESSED)
def main(files: tuple[BinaryIO], verbose: int, cmd: str, args: tuple[str]):
    # Logging framework is used for issues & debugging only, and outputs to stderr.
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(name)s: %(message)s", level=VERBOSE_OPTIONS[verbose])
    log = logging.getLogger("glscpc")

    click.echo(LOGO)

    if cmd is None:
        cmd = DEFAULT_COMMAND
        log.debug("No shellcheck command provided, defaulting to %r", cmd)
    else:
        cmd = shlex.split(cmd)
    cmd.extend(args)
    log.debug("Full command with arguments: %r", cmd)

    # A quick (not entirely bulletproof) sanity check, before we start computing.
    if shutil.which(cmd[0]) is None:
        click.secho(f"Cannot find executable {cmd[0]!r}. Is it installed?", fg="bright_red")
        raise Exit(2)

    exit_code = 0
    for file in files:
        # Only skip newline if verbosity is 0, that way everything can print on a single line if there is no problems.
        # But if we're verbose, there will be stderr log lines interleaved. Adding a newline makes that easier to read.
        click.secho(f"Processing {click.format_filename(file.name)}... ", fg="yellow", nl=verbose != 0)
        try:
            issues = "\n".join(transform_return(r) for r in process_file(file, cmd))
        except Exception as e:
            log.debug("Fatal error", exc_info=True)
            issues = transform_return(e)
        if issues:
            exit_code = 1
            click.secho("FAIL", fg="bright_red")
            click.echo(issues)
        else:
            click.secho("OK", fg="bright_green")
    raise Exit(exit_code)


if __name__ == "__main__":
    main()
