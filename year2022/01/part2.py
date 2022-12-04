large_calories = []
elf_count = 0
with open("test_inp.txt") as file:
    individual_callorie = 0
    for line in file:
        line = line.strip("\n")

        if line:
            individual_callorie += int(line)
        else:
            large_calories.append(individual_callorie)
            individual_callorie = 0
    else:
        large_calories.append(individual_callorie)

large_calories.sort(reverse=True)
print(large_calories[0] + large_calories[1] + large_calories[2])
