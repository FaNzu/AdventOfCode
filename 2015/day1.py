from pathlib import Path
import pytest

def get_data(filename):
    path = Path(__file__).parent / filename
    with path.open() as input_file:
        file_output = input_file.readline()
        return file_output

def get_part1_answer(data):
    floor = 0
    for char in data:
        if char == '(':
            floor += 1
        else:
            floor -= 1
    return floor


def get_part2_answer(data):
    floor = 0
    n = len(data)
    for i in range(n):
        if floor == -1:
            return i
        elif data[i] == '(':
            floor += 1
        else:
            floor -= 1


if __name__ == "__main__":
    input_data = get_data("data/day1_input.txt")
    print(f"Part1: {get_part1_answer(input_data)}")
    print(f"Part2: {get_part2_answer(input_data)}")