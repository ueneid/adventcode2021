from enum import Enum
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from util.util import read_lines_from_stdin


class Trend(Enum):
    NA = "N/A"
    INC = "increased"
    DEC = "decreased"


def get_reports_trend(reports: list[int]) -> list[Trend]:
    trends = []
    prev = None
    for r in reports:
        if prev is not None:
            if prev < r:
                trends.append(Trend.INC)
            elif prev > r:
                trends.append(Trend.DEC)
            else:
                trends.append(Trend.NA)
        else:
            trends.append(Trend.NA)
        prev = r
    return trends


def answer1(reports: list[int]) -> int:
    return get_reports_trend(reports).count(Trend.INC)


def answer2(reports: list[int], window_size: int = 3) -> int:
    new_reports = []
    for i, r in enumerate(reports):
        r_in_w = reports[i:i + window_size]
        if len(r_in_w) < window_size:
            break
        new_reports.append(sum(r_in_w))
    return answer1(new_reports)


if __name__ == "__main__":
    reports = read_lines_from_stdin(lambda lines: [int(line) for line in lines])
    print(answer1(reports))
    print(answer2(reports))
