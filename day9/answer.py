import sys
import pathlib

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + "/../")

from util.util import read_lines_from_stdin, echo


def answer1(matrix: list[list[int]]) -> int:
    adjacent_points = ((-1, 0), (1, 0), (0, -1), (0, 1))
    len_col = len(matrix)
    len_row = len(matrix[0])
    lower_points = []
    for i in range(len_col):
        for j in range(len_row):
            cur_height = matrix[i][j]
            adjacents = []
            for x, y in adjacent_points:
                ax, ay = j + x, i + y
                if not (0 <= ay < len_col and 0 <= ax < len_row):
                    continue
                adjacents.append(matrix[ay][ax])
            if cur_height not in adjacents and cur_height < min(adjacents):
                lower_points.append(cur_height)
    return sum([i + 1 for i in lower_points])


def answer2(matrix: list[list[int]]) -> int:
    adjacent_points = ((1, 0), (0, 1), (-1, 0), (0, -1))
    len_col = len(matrix)
    len_row = len(matrix[0])

    def bfs(cur_x: int, cur_y: int, basins: list[int] = []) -> list[int]:
        if not (0 <= cur_y < len_col and 0 <= cur_x < len_row):
            return basins
        cur_height = matrix[cur_y][cur_x]
        if cur_height == 9 or cur_height == -1:
            return basins
        matrix[cur_y][cur_x] = -1
        basins.append(cur_height)
        for x, y in adjacent_points:
            basins = bfs(cur_x + x, cur_y + y, basins)
        return basins

    basins_list = []
    for i in range(len_col):
        for j in range(len_row):
            basins = bfs(j, i, [])
            if basins:
                basins_list.append(basins)
    ret = 1
    for basins in sorted(basins_list, key=lambda x: len(x))[-3:]:
        ret *= len(basins)
    return ret


if __name__ == "__main__":

    def helper(lines: list[str]) -> list[list[int]]:
        matrix = []
        for line in lines:
            matrix.append([int(h) for h in list(line)])
        return matrix

    matrix = read_lines_from_stdin(helper)
    print(answer1(matrix))
    print(answer2(matrix))
