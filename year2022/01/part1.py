large_calorie = 0
with open("inp1.txt") as file:
    individual_callorie = 0
    for line in file:
        line = line.strip("\n")

        if line != "":
            individual_callorie += int(line)
        else:
            large_calorie = (
                individual_callorie
                if large_calorie < individual_callorie
                else large_calorie
            )
            individual_callorie = 0
            
    print(large_calorie)
