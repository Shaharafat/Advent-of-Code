with open("test_inp.txt") as file:
    for line in file:
        for (idx, char) in enumerate(line):
            four_char_set = set(line[idx : idx + 14])
            if len(four_char_set) == 14:
                break
            else:
                idx += 1
        print(idx + 14)
