import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

from util.util import read_lines_from_stdin, echo


def calc_distance(pivot: int, position: int) -> int:
    return abs(pivot - position)

def answer1(positions: list[int]) -> int:
    pivot = 0
    len_positions = len(positions)
    min_fuel = 99999999999
    while pivot < len_positions:
        tmp_min_fuel = 0
        for p in positions:
            tmp_min_fuel += calc_distance(pivot, p)
        min_fuel = min(min_fuel, tmp_min_fuel)
        pivot += 1
    return min_fuel

def answer2(positions: list[int]) -> int:
    pivot = 0
    len_positions = len(positions)
    min_fuel = 99999999999
    memo: dict[int, int] = {}
    while pivot < len_positions:
        tmp_min_fuel = 0
        for p in positions:
            distance = calc_distance(pivot, p)
            if fuel := memo.get(distance):
                tmp_min_fuel += fuel
            else:
                memo[distance] = sum(range(1, calc_distance(pivot, p) + 1))
                tmp_min_fuel += memo[distance]
        min_fuel = min(min_fuel, tmp_min_fuel)
        pivot += 1
    return min_fuel


if __name__ == "__main__":
    positions = read_lines_from_stdin(lambda lines: [int(x) for x in lines[0].split(",")])
    print(answer1(positions))
    print(answer2(positions))
