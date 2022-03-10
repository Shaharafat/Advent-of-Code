from utils.files import read_file


def part_1(input: str) -> int:
    content = read_file(input)
    floor = 0

    for char in content:
        if char == "(":
            floor = floor + 1
        if char == ")":
            floor = floor - 1

    return floor


def part_2(input: str) -> int:
    content = read_file(input)
    floor = 0

    for (index, char) in enumerate(content):
        if char == "(":
            floor = floor + 1
        if char == ")":
            floor = floor - 1

        if floor == -1:
            return index + 1


if __name__ == "__main__":
    filename = "year2015/inputs/day_1.txt"
    result = part_1(filename)
    print(result)
