with open("input.txt") as file:
    x = 1
    strength = 0
    cycle_count = 0
    crt_pixels = ""

    for line in file:
        line = line.strip("\n")
        if line.startswith("addx"):
            value = int(line.split(" ")[1])

            for i in range(0, 2):
                if cycle_count in [x - 1, x, x + 1]:
                    crt_pixels += "#"
                else:
                    crt_pixels += "."

                cycle_count += 1

                if cycle_count % 40 == 0:
                    crt_pixels += "\n"
                    cycle_count = 0

            x += value
        else:
            if cycle_count in [x - 1, x, x + 1]:
                crt_pixels += "#"
            else:
                crt_pixels += "."
            cycle_count += 1
            if cycle_count % 40 == 0:
                crt_pixels += "\n"
                cycle_count = 0

    print(crt_pixels)
