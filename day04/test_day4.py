import pytest
import day4 as aoc


@pytest.mark.parametrize("puzzle_input,expected",
    [
        (111111, True),
        (223450, False),
        (123789, False)
    ])
def test_part1(puzzle_input, expected):
    """Test part 1 on example input."""
    assert aoc.valid(puzzle_input) == expected

