with open("input.txt") as file:
    for line in file:
        for (idx, char) in enumerate(line):
            four_char_set = set(line[idx : idx + 4])
            if len(four_char_set) == 4:
                break
            else:
                idx += 1
        print(idx + 4)
