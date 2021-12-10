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
    last_board: list[list[int]] = []
    last_check_board: list[list[bool]] = []
    last_number = -1
    for chosen_number in chosen_numbers:
        board_index = 0
        while board_index < len(boards):
            board = boards[board_index]
            for j, row in enumerate(board):
                if chosen_number in row:
                    check_boards[board_index][j][row.index(chosen_number)] = True
            if is_bingo(check_boards[board_index]):
                last_board = boards.pop(board_index)
                last_check_board = check_boards.pop(board_index)
            else:
                board_index += 1
        if len(check_boards) == 0:
            last_number = chosen_number
            break
    score = 0
    for row, check_row in zip(last_board, last_check_board):
        score += sum([n for n, b in zip(row, check_row) if not b])
    return score * last_number


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
