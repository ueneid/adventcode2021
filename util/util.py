import sys
from typing import TypeVar, Callable, Optional

T = TypeVar("T")


def echo(arg: T) -> T:
    return arg


def read_from_stdin_as_array(cast_func: Callable[[str], T]) -> list[T]:
    return [cast_func(line.strip()) for line in sys.stdin]
