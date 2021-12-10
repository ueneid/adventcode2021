import sys
import pathlib
import copy
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

from util.util import read_lines_from_stdin, echo


def is_bingo(check_board: list[list[bool]]):
    for row in check_board:
        if all(row):
            return True
    for col in zip(*check_board):
        if all(col):
            return True


def answer1(chosen_numbers: list[int], boards: list[list[list[int]]], check_boards: list[list[list[bool]]]):
    for chosen_number in chosen_numbers:
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                if chosen_number in row:
                    check_boards[i][j][row.index(chosen_number)] = True
                    next
            if is_bingo(check_boards[i]):
                won_number = chosen_number
                score = 0
                for row, check_row in zip(board, check_boards[i]):
                    score += sum([n for n, b in zip(row, check_row) if not b])
                return score * won_number


def answer2(chosen_numbers: list[int], boards: list[list[list[int]]], check_boards: list[list[list[bool]]]):
    rest_boards = copy.deepcopy(boards)
    rest_check_boards = copy.deepcopy(check_boards)
    won_number = -999
    last_board, last_check_board = [], []
    for chosen_number in chosen_numbers:
        for i, board in enumerate(rest_boards):
            for j, row in enumerate(board):
                if chosen_number in row:
                    rest_check_boards[i][j][row.index(chosen_number)] = True
                    next
        copy_rest_boards = copy.deepcopy(rest_boards)
        copy_rest_check_boards = copy.deepcopy(rest_check_boards)
        rest_boards = []
        rest_check_boards = []
        for rb, rcb in zip(copy_rest_boards, copy_rest_check_boards):
            if not is_bingo(rcb):
                rest_boards.append(rb)
                rest_check_boards.append(rcb)
            else:
                won_number = chosen_number
                last_board = rb
                last_check_board = rcb
    score = 0
    for row, check_row in zip(last_board, last_check_board):
        score += sum([n for n, b in zip(row, check_row) if not b])
    return score * won_number


if __name__ == "__main__":
    def helper(lines: list[str]) -> tuple[list[int], list[list[list[int]]], list[list[list[bool]]]]:
        chosen_numbers = [int(n) for n in lines.pop(0).split(",")]
        boards: list[list[list[int]]] = []
        board: list[list[int]] = []
        row_count = 5
        for line in lines:
            if line == "":
                continue
            if row_count == 0:
                boards.append(board)
                board = []
                row_count = 5
            board.append([int(n) for n in line.split(" ") if n != ""])
            row_count -= 1
        boards.append(board)
        check_boards = [[[False] * 5 for _ in range(5)] for _ in range(len(boards))]
        return chosen_numbers, boards, check_boards

    chosen_numbers, boards, check_boards = read_lines_from_stdin(helper)
    print(answer1(copy.deepcopy(chosen_numbers), copy.deepcopy(boards), copy.deepcopy(check_boards)))
    print(answer2(copy.deepcopy(chosen_numbers), copy.deepcopy(boards), copy.deepcopy(check_boards)))
