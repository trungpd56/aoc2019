#!/usr/bin/env python3

import pathlib
import sys


class Console:
    def __init__(self, line):
        self.insts = [int(n) for n in line.strip().split(",")]

    def run(self):
        eip = 0
        while True:
            op = self.insts[eip]
            match op:
                case 1:
                    arg1 = self.insts[eip + 1]
                    arg2 = self.insts[eip + 2]
                    arg3 = self.insts[eip + 3]
                    self.insts[arg3] = self.insts[arg1] + self.insts[arg2]
                    eip += 4
                case 2:
                    arg1 = self.insts[eip + 1]
                    arg2 = self.insts[eip + 2]
                    arg3 = self.insts[eip + 3]
                    self.insts[arg3] = self.insts[arg1] * self.insts[arg2]
                    eip += 4
                case 99:
                    return self.insts[0]


def part1(data):
    """Solve part 1."""
    console = Console(data)
    console.insts[1] = 12
    console.insts[2] = 2
    return console.run()


def part2(data):
    """Solve part 2."""
    for noun in range(100):
        for verb in range(100):
            console = Console(data)
            console.insts[1] = noun
            console.insts[2] = verb
            if console.run() == 19690720:
                return 100 * noun + verb


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    solution1 = part1(puzzle_input)
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
