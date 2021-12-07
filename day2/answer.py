import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

from util.util import read_lines_from_stdin, echo


def answer1(commands: list[tuple[str, int]]) -> int:
    x, y = 0, 0
    for direction, value in commands:
        if direction == "forward":
            x += value
        if direction == "up":
            y -= value
        if direction == "down":
            y += value
    return x * y


def answer2(commands: list[tuple[str, int]]) -> int:
    x, y, aim = 0, 0, 0
    for direction, value in commands:
        if direction == "forward":
            x += value
            y += value * aim
        if direction == "up":
            aim -= value
        if direction == "down":
            aim += value
    return x * y


if __name__ == "__main__":
    commands = read_lines_from_stdin(lambda lines: [(direction, int(v)) for direction, v in [line.split(" ") for line in lines]])
    print(answer1(commands))
    print(answer2(commands))
