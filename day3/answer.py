import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

from util.util import read_lines_from_stdin, echo


def answer1(lines):
    bits = ""
    for line in zip(*lines):
        bits += "0" if line.count("0") > line.count("1") else "1"
    gamma = int("0b" + bits, 2)
    epsilon = ~gamma & int("0b" + "1" * len(bits), 2)
    return gamma * epsilon


def answer2(lines):
    pass


if __name__ == "__main__":
    lines = read_lines_from_stdin(echo)
    print(answer1(lines))
    print(answer2(lines))
