#!/usr/bin/env python3

import pathlib
import sys
from collections import defaultdict


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def solution(data: list, p2: bool = False) -> int:
    """Solve part 1."""
    dirs = dict(R=(1, 0), L=(-1, 0), D=(0, -1), U=(0, 1))
    paths = [defaultdict(int) for _ in range(2)]
    for i, line in enumerate(data):
        toks = line.split(",")
        x, y = 0, 0
        step = 0
        for tok in toks:
            val = int(tok[1:])
            dx, dy = dirs[tok[0]]
            for _ in range(val):
                x += dx
                y += dy
                step += 1
                paths[i][(x, y)] = step

    if not p2:
        dist = lambda x: abs(x[0]) + abs(x[1])
        return min(dist(p) for p in paths[0].keys() & paths[1].keys())
    return min(paths[0][p] + paths[1][p] for p in paths[0].keys() & paths[1].keys())


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = solution(data)
    solution2 = solution(data, p2=True)

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
