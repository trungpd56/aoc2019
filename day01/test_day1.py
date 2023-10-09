import pytest
import day1 as aoc


@pytest.mark.parametrize("puzzle_input,expected",
    [
        (12, 2),
        (14, 2),
        (1968, 654),
        (100756, 33583)
    ])
def test_cal(puzzle_input, expected):
    """Test part 1 on example input."""
    assert aoc.cal(puzzle_input) == expected

@pytest.mark.parametrize("puzzle_input,expected",
    [
        (14 , 2),
        (1969, 966),
        (100756, 50346)
    ])
def test_cal2(puzzle_input, expected):
    """Test part 2 on example input."""
    assert aoc.cal2(puzzle_input) == expected
