from day1 import get_data, get_part1_answer, get_part2_answer
import pytest

def test_day1_part1():
    data = get_data("data/day1_input.txt")
    answer = get_part1_answer(data)
    print(answer)
    assert answer == 232


def test_day1_part2():
    data = get_data("data/day1_input.txt")
    answer = get_part2_answer(data)
    assert answer == 1783