def compare_cycle_count_value(value):
    return value % 40 == 20


with open("test_inp.txt") as file:
    x = 1
    strength = 0
    cycle_count = 0
    for line in file:
        line = line.strip("\n")
        if line.startswith("addx"):
            value = int(line.split(" ")[1])
            if compare_cycle_count_value(cycle_count + 1):
                strength += (cycle_count + 1) * x
            elif compare_cycle_count_value(cycle_count + 2):
                strength += (cycle_count + 2) * x

            x += value
            cycle_count += 2
        else:
            if compare_cycle_count_value(cycle_count + 1):
                strength += (cycle_count + 1) * x
            cycle_count += 1
    
print(strength)
