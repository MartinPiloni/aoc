grid = []
instructions = ""
grid_parsing = True
r = c = -1
with open("day15.txt") as file:
    for line in file:
        if len(line.strip()) > 0 and grid_parsing:
            grid.append(line.strip())
        elif len(line.strip()) > 0:
            instructions += line.strip()
        else:
            grid_parsing = False

        # Look for the starting position
        if r == -1:
            for j in range(len(line)):
                if line[j] == "@":
                    r = len(grid) - 1
                    c = j


def move(r, c, dir):
    new_r = r + dir[0]
    new_c = c + dir[1]

    while grid[new_r][new_c] == "O":
        new_r += dir[0]
        new_c += dir[1]

    if grid[new_r][new_c] == "#":
        return r, c

    grid[new_r] = list(grid[new_r])
    grid[new_r][new_c] = "O"
    grid[new_r] = "".join(grid[new_r])

    grid[r] = list(grid[r])
    grid[r][c] = "."
    grid[r] = "".join(grid[r])

    r += dir[0]
    c += dir[1]

    grid[r] = list(grid[r])
    grid[r][c] = "@"
    grid[r] = "".join(grid[r])

    return r, c


moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for ins in instructions:
    if ins == "^":
        r, c = move(r, c, moves[0])
    elif ins == ">":
        r, c = move(r, c, moves[1])
    elif ins == "v":
        r, c = move(r, c, moves[2])
    elif ins == "<":
        r, c = move(r, c, moves[3])

ans1 = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "O":
            ans1 += i * 100 + j

print("Part 1:", ans1)
