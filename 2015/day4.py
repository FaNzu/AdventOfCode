from pathlib import Path

def get_data(filename):
    path = Path(__file__).parent / filename
    with path.open() as input_file:
        file_output = input_file.readline()
        return file_output


def part_one(data: str) -> int:
    return 

def part_two(data: str) -> int:
    return

if __name__ == "__main__":
    input_data = get_data("data/day4_input.txt")
    print(f"Part1: {part_one(input_data)}")
    print(f"Part2: {part_two(input_data)}")