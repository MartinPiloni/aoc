from collections import deque

grid = []
with open("day12.txt") as file:
    for line in file:
        grid.append(line.strip())


n = len(grid)
m = len(grid[0])
vis = {}


def valid(new_r, new_c):
    return 0 <= new_r < n and 0 <= new_c < m


def corner_contribution(r, c):
    ans = 0
    moves = {(-1, -1), (-1, 1), (1, -1), (1, 1)}

    for move in moves:
        new_r = r + move[0]
        new_c = c + move[1]

        if (
            valid(new_r, c)
            and grid[new_r][c] == grid[r][c]
            and valid(r, new_c)
            and grid[r][new_c] == grid[r][c]
            and valid(new_r, new_c)
            and grid[new_r][new_c] != grid[r][c]
        ):
            ans += 1
        elif (not valid(new_r, c) or grid[new_r][c] != grid[r][c]) and (
            not valid(r, new_c) or grid[r][new_c] != grid[r][c]
        ):
            ans += 1

    return ans


def bfs(sr, sc):
    moves = {(1, 0), (0, 1), (-1, 0), (0, -1)}

    area = 0
    perimeter = 0
    walls = 0
    q = deque()
    q.append((sr, sc))
    vis[(sr, sc)] = True
    while len(q) > 0:
        r, c = q[0]
        q.popleft()

        walls += corner_contribution(r, c)
        area += 1

        for move in moves:
            new_r = r + move[0]
            new_c = c + move[1]

            if (
                valid(new_r, new_c)
                and grid[new_r][new_c] == grid[r][c]
                and not (new_r, new_c) in vis
            ):
                q.append((new_r, new_c))
                vis[(new_r, new_c)] = True

            elif (
                not valid(new_r, new_c) or not grid[new_r][new_c] == grid[r][c]
            ):
                perimeter += 1

    return (area, perimeter, walls)


ans1 = ans2 = 0
for i in range(n):
    for j in range(m):
        if (i, j) not in vis:
            area, perimeter, walls = bfs(i, j)
            ans1 += area * perimeter
            ans2 += area * walls

print("Part 1:", ans1)
print("Part 2:", ans2)
