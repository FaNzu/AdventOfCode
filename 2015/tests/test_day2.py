from day2 import get_data, part_one, part_two
import pytest

@pytest.mark.parametrize('data, expected',
                        [
                            ([[2, 3, 4]], 58),
                            ([[4, 3, 2]], 58),
                            ([[1, 1, 10]], 43),
                            ([[2, 3, 4], [1, 1, 10]], 101),
                        ])
def test_day2_part1_example(data,expected):
    answer = part_one(data)
    assert answer == expected


@pytest.mark.parametrize('data, expected',
                        [
                            ([[2, 3, 4]], 34),
                            ([[4, 3, 2]], 34),
                            ([[1, 1, 10]], 14),
                            ([[2, 3, 4], [1, 1, 10]], 48),
                        ])
def test_day2_part2_example(data,expected):
    answer = part_two(data)
    assert answer == expected


def test_day2_part1():
    data = get_data("data/day2_input.txt")
    answer = part_one(data)
    assert answer == 1606483

def test_day2_part2():
    data = get_data("data/day2_input.txt")
    answer = part_two(data)
    assert answer == 3842356