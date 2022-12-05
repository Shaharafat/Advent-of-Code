with open("input.txt") as file:
    pairs = 0
    for line in file:
        line = line.strip("\n")
        section_one, section_two = line.split(",")
        x1, x2 = [int(n) for n in section_one.split("-")]
        y1, y2 = [int(n) for n in section_two.split("-")]
        if (x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2):
            pairs += 1

    print(pairs)
