#!/usr/bin/env python3

import pathlib
import sys
from collections import deque
from itertools import permutations, cycle


class Console:
    def __init__(self, line, inp):
        self.insts = [int(n) for n in line.strip().split(",")]
        self.inp = deque(inp)

    def run(self):
        eip = 0
        while True:
            cmd = format(self.insts[eip], "05d")
            _, m2, m1 = cmd[:3]
            match cmd[-2:]:
                case "01":
                    a1, a2, a3 = self.insts[eip + 1 : eip + 4]
                    self.insts[a3] = self.getval(a1, m1) + self.getval(a2, m2)
                    eip += 4
                case "02":
                    a1, a2, a3 = self.insts[eip + 1 : eip + 4]
                    self.insts[a3] = self.getval(a1, m1) * self.getval(a2, m2)
                    eip += 4
                case "03":
                    a1 = self.insts[eip + 1]
                    self.insts[a1] = self.inp.popleft()
                    eip += 2
                case "04":
                    a1 = self.insts[eip + 1]
                    return self.insts[a1]
                    eip += 2
                case "05":
                    a1, a2 = self.insts[eip + 1 : eip + 3]
                    if self.getval(a1, m1) != 0:
                        eip = self.getval(a2, m2)
                    else:
                        eip += 3
                case "06":
                    a1, a2 = self.insts[eip + 1 : eip + 3]
                    if self.getval(a1, m1) == 0:
                        eip = self.getval(a2, m2)
                    else:
                        eip += 3
                case "07":
                    a1, a2, a3 = self.insts[eip + 1 : eip + 4]
                    self.insts[a3] = int(
                        self.getval(a1, m1) < self.getval(a2, m2)
                    )
                    eip += 4
                case "08":
                    a1, a2, a3 = self.insts[eip + 1 : eip + 4]
                    self.insts[a3] = int(
                        self.getval(a1, m1) == self.getval(a2, m2)
                    )
                    eip += 4
                case "99":
                    return -1
                case _:
                    assert False

    def getval(self, a, m):
        if m == "1":
            return a
        return self.insts[a]


def part1(data):
    """Solve part 1."""
    cases = permutations(range(5))
    mt = 0
    for c in cases:
        out = None
        for phase in c:
            if out is None:
                inp = [phase, 0]
            else:
                inp = [phase, out]
            console = Console(data, inp)
            out = console.run()
        mt = max(mt, out)
    return mt


def part2(data):
    """Solve part 2."""
    # cases = permutations(range(5, 10))
    # prev = 0
    # for c in cases:
    #     out = None
    #     i = 0
    #     for phase in cycle(c):
    #         i += 1
    #         if out is None:
    #             inp = [phase, 0]
    #         else:
    #             inp = [phase, out]
    #         console = Console(data, inp)
    #         out = console.run()
    #         if out == -1:
    #             return prev
    #         else:
    #             prev = out


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    solution1 = part1(puzzle_input)
    solution2 = None

    return solution1, solution2


if __name__ == "__main__":
    infile = (
        sys.argv[1]
        if len(sys.argv) > 1
        else pathlib.Path(__file__).parent / "input.txt"
    )
    puzzle_input = pathlib.Path(infile).read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    if solution1:
        print(f" part1: {solution1}")
    if solution2:
        print(f" part2: {solution2}")
