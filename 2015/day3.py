from pathlib import Path

def get_data(filename):
    path = Path(__file__).parent / filename
    with path.open() as input_file:
        file_output = input_file.readline()
        return file_output


def deliver_packages(moves: str) -> set:
    
    directions = {'>': 1, '<': -1, '^': -1j, 'v': 1j}
    #1j is an imaginary number i use for coordinates

    houses = set()
    houses.add(0) # starting house

    current = 0
    for move in moves:
        current = current + directions[move]
        houses.add(current)

    return houses


def part_one(data: str) -> int:
    return len(deliver_packages(data))

def part_two(data: str) -> int:
    robot1_houses = deliver_packages(data[::2]) #a string with only every other char
    robot2_houses = deliver_packages(data[1::2]) #a string with only every other char, but starting 1 char further ahead
    all_houses = robot1_houses.union(robot2_houses) # takes only the none same ones
    return len(all_houses)

if __name__ == "__main__":
    input_data = get_data("data/day3_input.txt")
    print(f"Part1: {part_one(input_data)}")
    print(f"Part2: {part_two(input_data)}")