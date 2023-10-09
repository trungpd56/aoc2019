import pytest
import day2 as aoc


# @pytest.mark.parametrize("puzzle_input,expected",
#     [
#         ("1,0,0,0,99", "2,0,0,0,99"),
#         ("2,3,0,3,99", "2,3,0,6,99"),
#         ("2,4,4,5,99,0", "2,4,4,5,99,9801"),
#         ("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99"),
#     ])
# def test_part1(puzzle_input, expected):
#     """Test part 1 on example input."""
#     console = aoc.Console(puzzle_input)
#     assert console.run() == expected

@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("puzzle_input,expected",
    [
        ("", ""),
        ("", ""),
        ("", "")
    ])
def test_part2(puzzle_input, expected):
    """Test part 2 on example input."""
    parsed_input = aoc.parse(puzzle_input)
    assert aoc.part2(parsed_input) == expected
