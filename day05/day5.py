#!/usr/bin/env python3

import pathlib
import sys


class Console:
    def __init__(self, line, inp):
        self.insts = [int(n) for n in line.strip().split(",")]
        self.inp = inp

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
                case "99":
                    return self.insts[0]
                case "03":
                    a1 = self.insts[eip + 1]
                    self.insts[a1] = self.inp
                    eip += 2
                case "04":
                    a1 = self.insts[eip + 1]
                    print(self.insts[a1])
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
                    if self.getval(a1, m1) < self.getval(a2, m2):
                        self.insts[a3] = 1
                    else:
                        self.insts[a3] = 0
                    eip += 4
                case "08":
                    a1, a2, a3 = self.insts[eip + 1 : eip + 4]
                    if self.getval(a1, m1) == self.getval(a2, m2):
                        self.insts[a3] = 1
                    else:
                        self.insts[a3] = 0
                    eip += 4

    def getval(self, a, m):
        if m == "1":
            return a
        return self.insts[a]


def part1(data):
    """Solve part 1."""
    console = Console(data, 1)
    console.run()


def part2(data):
    """Solve part 2."""
    console = Console(data, 5)
    console.run()


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    print("Part1")
    solution1 = part1(puzzle_input)
    print("\nPart2")
    solution2 = part2(puzzle_input)

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

