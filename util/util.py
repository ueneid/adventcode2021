import sys
from typing import TypeVar, Callable, Optional

T = TypeVar("T")


def echo(arg: T) -> T:
    return arg


def read_lines_from_stdin(callback: Callable[[list[str]], T] = echo) -> T:
    inputs = [line.strip() for line in sys.stdin]
    return callback(inputs)
