#!/usr/bin/env python3

import pathlib
import sys
import re


def valid(num):
    nums = str(num)
    if re.search(r"(\d)\1", nums) and all(
        int(nums[i]) >= int(nums[i - 1]) for i in range(1, len(nums))
    ):
        return True
    return False


def parse(puzzle_input):
    """Parse input."""
    return list(map(int, puzzle_input.split("-")))


def part1(data):
    """Solve part 1."""
    return sum(valid(n) for n in range(*data))


def part2(data):
    """Solve part 2."""
    cnt = 0
    for n in range(*data):
        if valid(n) and any(len(g) == 2 for g, _ in re.findall(r"((\d)\2+)", str(n))):
            cnt += 1
    return cnt


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

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
