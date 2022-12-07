data_hash_map = {"/": {"parent": None, "total": 0}}
with open("test_inp.txt") as file:
    # This will store the whole directory map and total value
    parent = None
    current_dir = "/"
    for line in file:
        line = line.strip("\n")
        if line.startswith("$") and (len(line.split(" ")) == 3):
            if line.split(" ")[2] == "..":
                current_dir = data_hash_map[current_dir]["parent"]
            else:
                current_dir = line.split(" ")[2]

        elif line.startswith("$") and line.endswith("ls"):
            pass
        elif line.startswith("dir"):
            data_hash_map[line.split(" ")[1]] = {
                "parent": current_dir,
                "total": 0,
            }

        elif (not line.startswith("dir")) and (not line.startswith("$")):
            data_hash_map[current_dir][line.split(" ")[1]] = line.split(" ")[0]


# loop over the items
def traverse_and_calculate(data):
    total = 0
    for (i, v) in data.items():
        if (i != "parent") and (i != "total"):
            total += int(v)
    return int(total)


# traverse and calculate total
for (item, value) in data_hash_map.items():
    total = traverse_and_calculate(value)
    data_hash_map[item]["total"] = total
    # print(item)
    if data_hash_map[item]["parent"] != None:
        data_hash_map[data_hash_map[item]["parent"]]["total"] += total
        print(item, "adding to ", data_hash_map[data_hash_map[item]["parent"]])


print(data_hash_map)
