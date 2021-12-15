import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

from util.util import read_lines_from_stdin, echo


class Fish:
    init_timer_value_for_first_cycle = 8
    init_timer_value = 6

    def __init__(self, v: int, is_first_cycle: bool = False) -> None:
        self.timer = v
        self.is_first_cycle = is_first_cycle

    def reset_timer(self) -> None:
        if self.is_first_cycle:
            self.is_first_cycle = False
            self.timer = self.init_timer_value_for_first_cycle
        else:
            self.timer = self.init_timer_value

    def live_another_day(self):
        self.timer -= 1

    def spawn(self):
        return Fish(self.init_timer_value_for_first_cycle, False)


def answer1(fishes: list[Fish], days: int = 80):
    fishes2 = fishes
    for d in range(days):
        spawned_fishes = []
        for fish in fishes2:
            fish.live_another_day()
            if fish.timer < 0:
                fish.reset_timer()
                spawned_fishes.append(fish.spawn())
        fishes2 += spawned_fishes
        # print("After {} days: {}".format(d, [f.timer for f in fishes2]))
    return len(fishes2)


def answer2(lines):
    pass


if __name__ == "__main__":
    fishes = read_lines_from_stdin(lambda l: [Fish(int(f)) for f in l[0].split(",")])
    print(answer1(fishes))
    print(answer2(fishes))
