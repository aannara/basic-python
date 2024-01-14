from IPython.core.magic import register_line_cell_magic
import sys
import subprocess
from pathlib import Path
from IPython.display import display, HTML
import re

# Regular expression to match ANSI escape codes
ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")


def remove_ansi_escape_codes(text):
    return ansi_escape.sub("", text)


def save_and_run_magic(line, cell):
    commands = line.split()
    filename = "tmp.py"
    Path(filename).write_text(cell)

    process = subprocess.run(
        [sys.executable, "-m", *commands, filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    output = process.stdout
    error_output = process.stderr

    if output:
        display(HTML(f"<pre>{remove_ansi_escape_codes(output)}</pre>"))

    if error_output:
        display(
            HTML(
                f"<pre style='color: red;'>{remove_ansi_escape_codes(error_output)}</pre>"
            )
        )


def load_ipython_extension(ipython):
    ipython.register_magic_function(save_and_run_magic, magic_kind="line_cell")