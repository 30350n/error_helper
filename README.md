[![pypi](https://img.shields.io/pypi/v/error-helper)](https://pypi.org/project/error-helper/)
[![python](https://img.shields.io/badge/Python-3.6+-blue)](https://www.python.org/)
[![mit](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

# error-helper

This is a minimalistic python module which helps you print colorful messages for CLI
tools. It's available on [PyPi](https://pypi.org/project/error-helper/), but you can also add it
to your project as a git submodule.

## Usage

```pycon
>>> from error_helper import *
>>> info("this is information")                    # output will be blue
this is information
>>> hint("this is less important information")     # output will be grayed out
this is less important information
>>> warning("something didn't go quite right...")  # output will be yellow
warning: something didn't go quite right...
>>> error("something went terribly wrong")         # output will be red
error: something went terribly wrong
>>> success("completed the operation!")            # output will be green
successfully completed the operation!
```

### `prompt(...)` and `prompt_input(...)`

The `prompt(...)` function, by default, prints a newline, followed by the provided values,
a colon and another newline:

```pycon
>>> prompt("enter the server url")

enter the server url:
>>>
```

The `prompt_input(...)` function, by default, prints the provided values, followed by a colon
and a space. Then it calls the default `input(...)` function and returns it's result. The result
will be stripped if `strip=True` (default).

```pycon
>>> prompt("enter the server url"); url = prompt_input("url:")

enter the server url:
url:  https://30350n.de
>>> url
'https://30350n.de'
```
