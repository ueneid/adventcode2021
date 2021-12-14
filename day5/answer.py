import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

from util.util import read_lines_from_stdin, echo


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "x: {}, y: {}".format(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def is_horizontal(self) -> bool:
        return self.p1.y == self.p2.y

    def is_vertical(self) -> bool:
        return self.p1.x == self.p2.x

    def get_all_points(self) -> list[Point]:
        points: list[Point] = []
        for x in range(min(self.p1.x, self.p2.x), max(self.p1.x, self.p2.x) + 1):
            for y in range(min(self.p1.y, self.p2.y), max(self.p1.y, self.p2.y) + 1):
                points.append(Point(x, y))
        return points

    def __repr__(self) -> str:
        return "({}, {}) -> ({}, {})".format(self.p1.x, self.p1.y, self.p2.x, self.p2.y)


def answer1(vent_lines: list[Line]) -> int:
    diagram: dict[Point, int] = {}
    for line in vent_lines:
        if not (line.is_horizontal() or line.is_vertical()):
            continue
        for point in line.get_all_points():
            if point in diagram:
                diagram[point] += 1
            else:
                diagram[point] = 1
    return len([v for v in diagram.values() if v > 1])

def answer2(lines):
    pass


if __name__ == "__main__":
    def helper(lines: list[str]) -> list[Line]:
        ret: list[Line] = []
        for line in lines:
            points: list[Point] = []
            for start_end_points in line.split(" -> "):
                x, y = [p for p in start_end_points.split(",")]
                points.append(Point(int(x), int(y)))
            ret.append(Line(*points))
            points = []
        return ret
    vent_lines = read_lines_from_stdin(helper)
    print(answer1(vent_lines))
    print(answer2(vent_lines))
