from pathlib import Path
import re
from typing import List

def get_data(filename: str) -> List[List[int]]:
    path = Path(__file__).parent / filename
    return [extract_numbers(line) for line in path.open().readlines()]

def extract_numbers(data: str) -> list[int]:
    return list(map(int, re.findall(r'[-\d]+', data)))

def part_one(data: list[str]) -> int:
    totalPaper: int = 0
    for box in data:
        length, width, height = sorted(box)
        areal, small = presentBox(length, width, height)
        totalPaper += areal + small
    return totalPaper

def part_two(data: list[str]) -> int:
    totalRibbon = 0
    for box in data:
        length, width, height = sorted(box)
        ribbon = 2 * length + 2 * width
        bow = length * width * height
        totalRibbon += ribbon + bow
    return totalRibbon

def presentBox(length: int, width: int, height: int):
    side1 = length * width
    side2 = width * height
    side3 = height * length
    
    BoxAreal: int = 2*side1 + 2*side2 + 2*side3
    SmallAreal: int = min([side1, side2, side3])
    
    
    return BoxAreal, SmallAreal

if __name__ == "__main__":
    input_data = get_data("data/day2_input.txt")
    print(f"Part1: {part_one(input_data)}")
    print(f"Part2: {part_two(input_data)}")