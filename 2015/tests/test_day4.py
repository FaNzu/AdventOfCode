from day3 import get_data, part_one, part_two
import pytest

@pytest.mark.parametrize('data, expected',
                        [
                            ('>', 2),
                            ('^>v<', 4),
                            ('^v^v^v^v^v', 2),
                        ])
def test_day3_part1_example(data,expected):
    answer = part_one(data)
    assert answer == expected


@pytest.mark.parametrize('data, expected',
                        [
                            ('^v', 3),
                            ('^>v<', 3),
                            ('^v^v^v^v^v', 11),
                        ])
def test_day3_part2_example(data,expected):
    answer = part_two(data)
    assert answer == expected


def test_day3_part1():
    data = get_data("data/day3_input.txt")
    answer = part_one(data)
    assert answer == 2565

def test_day3_part2():
    data = get_data("data/day3_input.txt")
    answer = part_two(data)
    assert answer == 2639