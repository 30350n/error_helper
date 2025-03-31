from sys import stderr as _stderr
from typing import TextIO

COLOR_INFO = "\033[94m"
COLOR_HINT = "\033[2;3m"
COLOR_PROMPT = ""
COLOR_SUCCESS = "\033[92m"
COLOR_WARNING = "\033[93m"
COLOR_ERROR = "\033[91m"
COLOR_END = "\033[0m"

BOLD = "\033[1m"
BOLD_END = "\033[22m"

ITALIC = "\033[3m"
ITALIC_END = "\033[23m"

CLEAR_LINE = "\033[2K"

INFO_END = "\n"
_last_end = INFO_END


def info(
    *values: object,
    sep: str = " ",
    end: str | None = None,
    file: TextIO | None = None,
    flush: bool = False,
):
    global _last_end
    output = f"{CLEAR_LINE}{COLOR_INFO}{sep.join(map(str, values))}{COLOR_END}"
    end = INFO_END if end is None else end
    print(output, end=end, flush=flush, file=file)
    _last_end = end


def hint(
    *values: object,
    sep: str = " ",
    end: str | None = "\n",
    file: TextIO | None = None,
    flush: bool = False,
):
    global _last_end
    output = f"{CLEAR_LINE}{COLOR_HINT}({sep.join(map(str, values))}){COLOR_END}"
    print(output, end=end, flush=flush, file=file)
    _last_end = end


def prompt(
    *values: object,
    sep: str = " ",
    end: str | None = ":\n",
    file: TextIO | None = None,
    flush: bool = False,
    prefix: str = "\n",
):
    global _last_end
    output = f"{CLEAR_LINE}{COLOR_PROMPT}{prefix}{sep.join(map(str, values))}{COLOR_END}"
    print(output, end=end, flush=flush, file=file)
    _last_end = end


def prompt_input(*values: object, end: str | None = ": ", strip: bool = True):
    prompt(*values, end=end, prefix="")
    return input().strip() if strip else input()


def success(
    *values: object,
    sep: str = " ",
    end: str | None = "\n",
    file: TextIO | None = None,
    flush: bool = False,
    prefix: str = "successfully ",
):
    global _last_end
    output = f"{CLEAR_LINE}{COLOR_SUCCESS}{prefix}{sep.join(map(str, values))}{COLOR_END}"
    print(output, end=end, flush=flush, file=file)
    _last_end = end


def warning(
    *values: object,
    sep: str = " ",
    end: str | None = "\n",
    file: TextIO | None = None,
    flush: bool = False,
    prefix: str = "warning: ",
):
    global _last_end
    output = f"{CLEAR_LINE}{COLOR_WARNING}{prefix}{sep.join(map(str, values))}{COLOR_END}"
    print(output, end=end, flush=flush, file=file)
    _last_end = end


def error(
    *values: object,
    sep: str = " ",
    end: str | None = "\n",
    file: TextIO | None = _stderr,
    flush: bool = False,
    prefix: str = "error: ",
):
    global _last_end
    extra_prefix = "" if _last_end and _last_end[-1] == "\n" else "\n"
    output = f"{extra_prefix}{COLOR_ERROR}{prefix}{sep.join(map(str, values))}{COLOR_END}"
    print(output, end=end, flush=flush, file=file)
    _last_end = end
