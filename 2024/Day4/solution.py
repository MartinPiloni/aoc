def valid(grid, r, c):
    return r >= 0 and r < len(grid) and c >= 0 and c <= len(grid[r])


def find_xmas_occ(grid, r, c):
    xmas = "XMAS"
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]
    ans = 0
    for dir in directions:
        found = True
        for i in range(4):
            new_r = r + dir[0] * i
            new_c = c + dir[1] * i
            if not valid(grid, new_r, new_c) or grid[new_r][new_c] != xmas[i]:
                found = False
                break

        if found:
            ans += 1

    return ans


def valid2(n, m, left, right, up, down):
    return left >= 0 and up >= 0 and right < m and down < n


def find_mas(grid, r1, c1, r2, c2):
    if (grid[r1][c1] == "M" and grid[r2][c2] == "S") or (
        grid[r1][c1] == "S" and grid[r2][c2] == "M"
    ):
        return True
    return False


def find_cross_mas_occ(grid, r, c):
    up = r - 1
    down = r + 1
    left = c - 1
    right = c + 1

    if grid[r][c] != "A" or not valid2(
        len(grid), len(grid[r]), left, right, up, down
    ):
        return 0

    if find_mas(grid, up, left, down, right) and find_mas(
        grid, up, right, down, left
    ):
        return 1

    return 0


input = []
with open("day4.txt") as file:
    for line in file:
        input.append(line)

ans1 = ans2 = 0
for i in range(len(input)):
    for j in range(len(input[i])):
        ans1 += find_xmas_occ(input, i, j)
        ans2 += find_cross_mas_occ(input, i, j)

print("Part 1:", ans1)
print("Part 2:", ans2)
