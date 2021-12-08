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


def divide_bit_list(bits: list[str], index: int) -> tuple[list[str], list[str]]:
    bit0, bit1 = [], []
    for bit in bits:
        if bit[index] == "0":
            bit0.append(bit)
        else:
            bit1.append(bit)
    return bit0, bit1


def get_oxygen_generator_rating(lines: list[str]) -> int:
    bits = lines
    index = 0
    while bits:
        if len(bits) == 1:
            break
        bit0, bit1 = divide_bit_list(bits, index)
        len_bit0, len_bit1 = len(bit0), len(bit1)
        if len_bit0 <= len_bit1:
            bits = bit1
        else:
            bits = bit0
        index += 1
    return int("0b" + bits[0], 2)


def get_CO2_scrubber_rating(lines: list[str]) -> int:
    bits = lines
    index = 0
    while bits:
        if len(bits) == 1:
            break
        bit0, bit1 = divide_bit_list(bits, index)
        len_bit0, len_bit1 = len(bit0), len(bit1)
        if len_bit0 > len_bit1:
            bits = bit1
        else:
            bits = bit0
        index += 1
    return int("0b" + bits[0], 2)


def answer2(lines) -> int:
    return get_oxygen_generator_rating(lines) * get_CO2_scrubber_rating(lines)


if __name__ == "__main__":
    lines = read_lines_from_stdin(echo)
    print(answer1(lines))
    print(answer2(lines))
