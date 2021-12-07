import enum
import sys
from enum import Enum


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
    reports = []
    for l in sys.stdin:
        reports.append(int(l))
    print(answer1(reports))
    print(answer2(reports))
