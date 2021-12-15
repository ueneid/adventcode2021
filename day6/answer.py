import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

from util.util import read_lines_from_stdin, echo


def answer1(lines):
    pass


def answer2(lines):
    pass


if __name__ == "__main__":
    lines = read_lines_from_stdin(echo)
    print(answer1(lines))
    print(answer2(lines))
