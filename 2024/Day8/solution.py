grid = []
with open("day8.txt") as file:
    for line in file:
        grid.append(line.strip())

n = len(grid)
m = len(grid[0])


def valid(r, c):
    return 0 <= r < n and 0 <= c < m


def count_antinodes(r, c, count, count2):
    for i in range(r, n):
        for j in range(m):
            if i == r and j <= c:
                continue

            if grid[i][j] == grid[r][c]:
                r_offset = i - r
                c_offset = j - c

                k = 0
                while valid(r - r_offset * k, c - c_offset * k):
                    if k == 1:
                        count.add((r - r_offset * k, c - c_offset * k))
                    count2.add((r - r_offset * k, c - c_offset * k))
                    k += 1

                k = 0
                while valid(i + r_offset * k, j + c_offset * k):
                    if k == 1:
                        count.add((i + r_offset * k, j + c_offset * k))
                    count2.add((i + r_offset * k, j + c_offset * k))
                    k += 1

    return


count = set()
count2 = set()
for i in range(n):
    for j in range(m):
        if grid[i][j] != ".":
            count_antinodes(i, j, count, count2)

ans1 = len(count)
ans2 = len(count2)
print("Part 1:", ans1)
print("Part 2:", ans2)
