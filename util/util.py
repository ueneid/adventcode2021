import sys
from typing import TypeVar, Callable

T = TypeVar("T")


def read_from_stdin_as_array(cast_func: Callable[[str], T]) -> list[T]:
    return [cast_func(line) for line in sys.stdin]
