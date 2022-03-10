# from utils.files import read_file
# def read_file(file: str) -> str:
#     with open(file, "r") as buf:
#         content = buf.read()

#     return content


def part_1(input: str) -> int:
    total_square_feet = 0
    # open file
    content = open(input)
    count = 0
    line = content.readline().split("x")
    while len(line) == 3:
        count += 1

        l = int(line[0])
        w = int(line[1])
        h = int(line[2])
        lw = l * w
        wh = w * h
        hl = h * l
        minArea = min(lw, wh, hl)

        total_square_feet += (2 * lw) + (2 * wh) + (2 * hl) + minArea
        line = content.readline().split("x")

    # close file
    content.close()
    return total_square_feet


# if __name__ == "__main__":
#     part_1("year2015/inputs/day_2/part_1_test_1.txt")
#     part_1("year2015/inputs/day_2/part_1_test_inp.txt")
