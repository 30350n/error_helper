import sys

COLOR_INFO = "\033[94m"
COLOR_HINT = "\033[2;3m"
COLOR_SUCCESS = "\033[92m"
COLOR_WARNING = "\033[93m"
COLOR_ERROR = "\033[91m"
COLOR_END = "\033[0m"

INFO_END = "\n"
CLEAR_LINE = "\033[2K"

def info(*values, sep=" ", end=None, file=sys.stdout, flush=False):
    output = f"{CLEAR_LINE}{COLOR_INFO}{sep.join(map(str, values))}{COLOR_END}"
    end = INFO_END if end is None else end
    print(output, end=end, flush=flush, file=file)

def hint(*values, sep=" ", end="\n", file=sys.stdout, flush=False):
    output = f"{CLEAR_LINE}{COLOR_HINT}({sep.join(map(str, values))}){COLOR_END}"
    print(output, end=end, flush=flush, file=file)

def success(*values, sep=" ", end="\n", file=sys.stdout, flush=False, prefix="successfully "):
    output = f"{CLEAR_LINE}{COLOR_SUCCESS}{prefix}{sep.join(map(str, values))}{COLOR_END}"
    print(output, end=end, flush=flush, file=file)

def warning(*values, sep=" ", end="\n", file=sys.stdout, flush=False, prefix="warning: "):
    output = f"{CLEAR_LINE}{COLOR_WARNING}{prefix}{sep.join(map(str, values))}{COLOR_END}"
    print(output, end=end, flush=flush, file=file)

def error(*values, sep=" ", end="\n", file=sys.stderr, flush=False, prefix="error: "):
    output = f"{CLEAR_LINE}{COLOR_ERROR}{prefix}{sep.join(map(str, values))}{COLOR_END}"
    print(output, end=end, flush=flush, file=file)
