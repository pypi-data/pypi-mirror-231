import json
import logging
import subprocess
from typing import Any, BinaryIO

import click
import ruamel.yaml
import ruamel.yaml.comments
from ruamel.yaml.scalarstring import LiteralScalarString

"""
Documentation used to create this file: https://docs.gitlab.com/ee/ci/yaml/index.html

Important things of note:
- before_script and script are concatenated in reality, but we don't do that to keep track of line numbers.
- Unused (template) scripts are also checked.
"""

LOG = logging.getLogger("glscpc")

INCLUDE = "include"
GLOBAL_KEYWORDS = {
    # Default is missing because it also has script keys, we want to treat it like a job.
    INCLUDE,
    "stages",
    "variables",
    "workflow",
    "image",
    "services",
    "cache",
    "before_script",  # Deprecated (ignored by glscpc!)
    "after_script",  # Deprecated (ignored by glscpc!)
}

COLORS = {
    "error": "red",
    "warning": "yellow",
    "info": "green",
    "style": "green",
    "verbose": "green",
    "message": "bold",
    "source": None,
}


class Issue(Exception):
    def __init__(self, message: str, file: BinaryIO, obj: Any, line: int | None = None, print_type_value=True):
        self.formatted_message = f"{message} in file {file.name!r}"
        if line is not None:
            self.formatted_message += f" on line {line+1}"
        if print_type_value:
            self.formatted_message += f"\n\ttype: {type(obj)}, value: {obj!r}"

    def __str__(self) -> str:
        return self.formatted_message


def process_file(file: BinaryIO, cmd: list[str]):
    """
    Process a gitlab-ci file. File must be valid and well-formed for proper functioning of this function.
    Raises or yields nothing if all is good.
    Fatal issues cause raised exceptions (invalid yaml etc)
    Other issues are yielded so they can be handled by the caller as needed.

    To be able to keep track of the file, key & position information, we nest the inner functions.
    """
    # Load the YAML file with round-trip loader, meaning it preserves comment & line nr info to allow dumping later.
    # We abuse this and the required "internals" to get the line nr information from the undocumented .lc attributes.
    # To get the line info for a dict entry, you need to use <parent>.lc.key(<name>)[0] (index 1 would be the column).
    # For an array entry, replace .key(<name>) with .item(<index>).
    # Beware: ruamel.yaml's data is 0 indexed, shellcheck is 1 indexed.
    yaml = ruamel.yaml.YAML(typ="rt")
    root = yaml.load(file)
    if not isinstance(root, ruamel.yaml.comments.CommentedMap):
        raise Issue("The given file root object is not a map", file, root)

    if INCLUDE in root:
        # This is far too complex to handle without a concrete usecase.
        raise Issue("Including other files is not supported", file, root[INCLUDE], line=root.lc.key(INCLUDE)[0], print_type_value=False)

    for job_name, job_data in root.items():
        # Do not skip over templates (.-prefixed) or defaults, then we don't have to do inheritance later.
        if job_name in GLOBAL_KEYWORDS:
            if "script" in job_name:
                yield Issue(
                    f"Global script keywords are deprecated and not checked by this tool!", file, job_name, root.lc.key(job_name)[0]
                )
            continue
        if not isinstance(job_data, ruamel.yaml.comments.CommentedMap):
            raise Issue(f"Job {job_name!r} object is not a map.", file, job_data, root.lc.key(job_name)[0])
        LOG.debug("Processing job %r", job_name)

        def process_section(key):
            LOG.debug("Processing %s", key)
            # Make some assertions about the data types. A section must be a CommentedSeq[str] as that retains line nr info.
            if not isinstance(seq, ruamel.yaml.comments.CommentedSeq):
                raise Issue(f"Job {job_name!r} {key} object is not a sequence.", file, seq, job_data.lc.key(key)[0])
            for idx, item in enumerate(seq):
                if not isinstance(item, str):
                    raise Issue(f"Job {job_name!r} {key} entry {idx+1} is not a string.", file, item, seq.lc.item(idx)[0])

            # OK now we're reasonably sure that every item in the script sequence is at least a str derivative
            # Now we concat the entire thing and hand it to shellcheck and parse it's json output.
            # It would be simpler to check every item individually, but that isn't how it works when running.
            # The json1 output format is not properly documented.
            LOG.debug("Merged script, as passed to shellcheck:\n%s", "\n".join(seq))
            result = subprocess.run(cmd, input="\n".join(seq), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            # 0 means no issues found, so we can return early without yielding any issues.
            if result.returncode == 0:
                return

            # Shellcheck has some remarks, let the fun begin.
            issues = json.loads(result.stdout)["comments"]
            # Sort here based on line number, so we can handle the issues sequentially and guarantee we don't skip lines that need comments
            # Within a line we sort based on reverse column so the first issues text doesn't overlap with the position idicator bar for subsequent issues.
            issues.sort(key=lambda x: (x["line"], -x["column"]))
            LOG.debug("Issues: %r", issues)

            yield click.style(
                f"Issue(s) in job {job_name!r} {key} in file {file.name!r} with merged script (line numbers are estimates):", fg="red"
            )

            # We'd like to accurately report the line nr of the issue, but yaml is !fun! when it comes to strings.
            # https://yaml-multiline.info/
            # So the joined script we passed to shellcheck isn't likely to look like the yaml file.
            # Thus, we need line accounting.

            # This bit of magic allows us to iterate over the issues outside a for/while loop, since we only want to go to the next once
            # we've done processing it, which may take any number of lines in the script to happen.
            issue_iterator = iter(issues)
            i = next(issue_iterator)

            # Line number as passed to ShellCheck. Incremented for every line in the merged output.
            # Not shown to user, because it bears no direct relation to the line nr in the yml file.
            # Required to match up issues with their respective lines in the ShellScript input.
            script_line_nr = 0

            # Every item in seq is a string. They are all joined by newlines into the script gitlab runs, but we can't just glue then if we
            # want accurate line numbers from the yaml file because there are many different forms of yaml multiline strings.
            # In a simpler world, every item would be a single line of shell code and it would be easy, but it's not.
            item: str
            for idx, item in enumerate(seq):
                # Line number of the start of this item in the script array.
                source_line = seq.lc.item(idx)[0]
                # If this is a "Literal Scalar" style string (- |\n...), the actual string starts only on the next line, so +1
                # "Folded Scalar" styles strings (- >) fold the newlines into spaces, which messes up our tracking.
                # This is ignored since they are far less common in scripts and handling it would require significant added complexity.
                # Chomping (strip -, clip or keep +) of newlines only affects newlines at the end of the script, so we don't care here.
                # Multiline quoted strings are undetectable and may cause issues with line number accounting.
                if isinstance(item, LiteralScalarString):
                    source_line += 1

                line: str
                # .split(\n) instead of .splitlines because we need to get an entry for every line, including empty last lines.
                for line_index, line in enumerate(item.split("\n")):
                    # pre-increment because it keeps the code together and the first line must start at 1 anyway.
                    script_line_nr += 1
                    # items in the script sequence are merged with newlines, so add 1 to account for the extra line.
                    yml_line = source_line + line_index + 1

                    yield f'{click.style(f"{yml_line:4} │", fg="cyan")} {line}'
                    # As long as the current issue (incremented at the bottom of the while) is related to the current line:
                    while i["line"] == script_line_nr:
                        prefix_len = 6
                        # Inclusive numbering, so -2 to get only the parts between the corner bits.
                        # If we're taling about a single character, we'll end up printing a 2 wide indicator. Oh well.
                        bar = "─" * max(0, i["endColumn"] - i["column"] - 2)
                        message = f'{i["level"]}: {i["message"]}'
                        # If it fits, print the mess age before the position bar to keep the overal line lengt sane (prevents hard-wraps)
                        if i["column"] < len(message):
                            indent = " " * (i["column"] + prefix_len)
                            comment = click.style(f"{indent}└{bar}┘ {message}", fg=COLORS.get(i["level"]))
                        else:
                            indent = " " * (i["column"] - len(message) - 2)  # -2 to account for 2 spaces in f-string
                            comment = click.style(f'{" " * prefix_len} {message}{indent} └{bar}┘', fg=COLORS.get(i["level"]))
                        yield comment
                        # Go to the next issue or exit the while loop if there are none left.
                        # We don't have to exit the for loop(s) because i[line] will never be == script_line_nr anymore,
                        # so we'll never enter the while after the last indicator anymore.
                        # By not exiting the for we still print the rest of the script without needing additional special logic.
                        try:
                            i = next(issue_iterator)
                        except StopIteration:
                            # If there are not more issues, we can stop processing this while loop.
                            break
                    # todo: Compute fix suggestion. Effort abandoned due to extensive processing required.
                    #   The fix array contains a list of operations to do on the original line, but they also all
                    #   have influence on the output line, so it's not so easy to just apply them sequentially.

        if seq := job_data.mlget(["hooks", "pre_get_sources_script"]):
            yield from process_section("hooks:pre_get_sources_script")
        if seq := job_data.get("before_script"):
            yield from process_section("before_script")
        if seq := job_data.get("script"):
            yield from process_section("script")
        if seq := job_data.get("after_script"):
            yield from process_section("after_script")
