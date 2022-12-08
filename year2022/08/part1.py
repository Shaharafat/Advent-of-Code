grid = []
with open("input.txt") as file:
    for line in file:
        line = line.strip("\n")

        row = [int(x) for x in list(line)]
        grid.append(row)


edge_visibility_count = (len(grid) * 2) + ((len(grid[0]) - 2) * 2)
row_count = len(grid)
col_count = len(grid[0])

inside_visibility_count = set()
for i in range(1, row_count - 1):
    for j in range(1, col_count - 1):
        char = grid[i][j]
        try:
            next(e for e in grid[i][:j] if e >= char)
            next(e for e in grid[i][j + 1 :] if e >= char)
            next(grid[i2][j] for i2 in list(range(0, i)) if grid[i2][j] >= char)
            next(
                grid[i2][j]
                for i2 in list(range(i + 1, row_count))
                if grid[i2][j] >= char
            )
        except StopIteration:
            edge_visibility_count += 1


print(edge_visibility_count)
