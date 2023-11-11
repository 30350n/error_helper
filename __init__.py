from sys import stderr as _stderr

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

INFO_END = "\n"
_LAST_END = [INFO_END]
CLEAR_LINE = "\033[2K"

def info(*values, sep=" ", end=None, file=None, flush=False):
    output = f"{CLEAR_LINE}{COLOR_INFO}{sep.join(map(str, values))}{COLOR_END}"
    end = INFO_END if end is None else end
    print(output, end=end, flush=flush, file=file)
    _LAST_END[0] = end

def hint(*values, sep=" ", end="\n", file=None, flush=False):
    output = f"{CLEAR_LINE}{COLOR_HINT}({sep.join(map(str, values))}){COLOR_END}"
    print(output, end=end, flush=flush, file=file)
    _LAST_END[0] = end

def prompt(*values, sep=" ", end=":\n", file=None, flush=False, prefix="\n"):
    output = f"{CLEAR_LINE}{COLOR_PROMPT}{prefix}{sep.join(map(str, values))}{COLOR_END}"
    print(output, end=end, flush=flush, file=file)
    _LAST_END[0] = end

def prompt_input(*values, end=": ", strip=True):
    prompt(*values, end=end, prefix="")
    return input().strip() if strip else input()

def success(*values, sep=" ", end="\n", file=None, flush=False, prefix="successfully "):
    output = f"{CLEAR_LINE}{COLOR_SUCCESS}{prefix}{sep.join(map(str, values))}{COLOR_END}"
    print(output, end=end, flush=flush, file=file)
    _LAST_END[0] = end

def warning(*values, sep=" ", end="\n", file=None, flush=False, prefix="warning: "):
    output = f"{CLEAR_LINE}{COLOR_WARNING}{prefix}{sep.join(map(str, values))}{COLOR_END}"
    print(output, end=end, flush=flush, file=file)
    _LAST_END[0] = end

def error(*values, sep=" ", end="\n", file=_stderr, flush=False, prefix="error: "):
    PREFIX = "" if _LAST_END[0] and _LAST_END[0][-1] == "\n" else "\n"
    output = f"{PREFIX}{COLOR_ERROR}{prefix}{sep.join(map(str, values))}{COLOR_END}"
    print(output, end=end, flush=flush, file=file)
    _LAST_END[0] = end
