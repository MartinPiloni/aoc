grid = []
with open("day10.txt") as file:
    for line in file:
        grid.append(line.strip())

n = len(grid)
m = len(grid[0])
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def valid(r, c):
    return 0 <= r < n and 0 <= c < m


def bfs(sr, sc):
    cnt = 0
    vis = set()
    vis.add((sr, sc))

    q = [(sr, sc)]
    while len(q) > 0:
        r, c = q[0]
        q.pop(0)

        height = int(grid[r][c])
        if height == 9:
            cnt += 1
            continue

        for move in moves:
            new_r = r + move[0]
            new_c = c + move[1]

            if (
                valid(new_r, new_c)
                and not (new_r, new_c) in vis
                and int(grid[new_r][new_c]) == height + 1
            ):
                q.append((new_r, new_c))
                vis.add((new_r, new_c))

    return cnt


def bfs2(sr, sc):
    cnt = 0
    q = [(sr, sc)]
    while len(q) > 0:
        r, c = q[0]
        q.pop(0)

        height = int(grid[r][c])
        if height == 9:
            cnt += 1
            continue

        for move in moves:
            new_r = r + move[0]
            new_c = c + move[1]

            if valid(new_r, new_c) and int(grid[new_r][new_c]) == height + 1:
                q.append((new_r, new_c))

    return cnt


ans1 = ans2 = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "0":
            ans1 += bfs(i, j)
            ans2 += bfs2(i, j)

print("Part 1:", ans1)
print("Part 2:", ans2)
