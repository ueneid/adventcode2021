import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

from util.util import read_lines_from_stdin, echo


class DigitDisplay:
    def __init__(self, signals: list[str], outputs: list[str]) -> None:
        self.signals = signals
        self.outputs = outputs

    def build_segments(self):
        self.segments = {}
        len_5_segments = []
        len_6_segments = []
        for s in self.signals:
            len_s = len(s)
            set_s = set(s)
            if len_s == 2:
                self.segments["1"] = set_s
            elif len_s == 3:
                self.segments["7"] = set_s
            elif len_s == 4:
                self.segments["4"] = set_s
            elif len_s == 7:
                self.segments["8"] = set_s
            elif len_s == 5:
                len_5_segments.append(set_s)
            else:
                len_6_segments.append(set_s)
        for s in len_5_segments:
            if len(s - self.segments["1"]) == 3:
                self.segments["3"] = s
            else:
                len_rest_seg = len(s - self.segments["4"])
                if len_rest_seg == 2:
                    self.segments["5"] = s
                else:
                    self.segments["2"] = s
        for s in len_6_segments:
            if len(s - self.segments["3"]) == 1:
                self.segments["9"] = s
            elif len(s - self.segments["5"]) == 1:
                self.segments["6"] = s
            else:
                self.segments["0"] = s

    def get_digit(self) -> int:
        digit = ""
        for o in self.outputs:
            for k, v in self.segments.items():
                if set(o) == v:
                    digit += k
                    break
        return int(digit)

    def __repr__(self) -> str:
        return "<s: {} o: {}>".format(",".join(self.signals), ",".join(self.outputs))


def answer1(digit_displays: list[DigitDisplay]) -> int:
    counter = 0
    unique_segments = (2, 3, 4, 7)
    for digit_display in digit_displays:
        counter += sum([1 for o in digit_display.outputs if len(o) in unique_segments])
    return counter


def answer2(digit_displays: list[DigitDisplay]):
    digits = [d.build_segments() or d.get_digit() for d in digit_displays]
    return sum(digits)

if __name__ == "__main__":
    def helper(lines: list[str]) -> list[DigitDisplay]:
        digit_displays: list[DigitDisplay] = []
        for line in lines:
            signal, output = line.split(" | ")
            digit_displays.append(DigitDisplay(signal.split(" "), output.split(" ")))
        return digit_displays
    digit_displays = read_lines_from_stdin(helper)
    print(answer1(digit_displays))
    print(answer2(digit_displays))
