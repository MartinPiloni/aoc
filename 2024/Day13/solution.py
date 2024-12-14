import re

a_list = []
b_list = []
prize_list = []
with open("day13.txt") as file:
    idx = 0
    for line in file:
        if idx % 4 == 0:
            a_list.append(re.findall(r"\d+", line))
        elif idx % 4 == 1:
            b_list.append(re.findall(r"\d+", line))
        elif idx % 4 == 2:
            prize_list.append(re.findall(r"\d+", line))

        idx += 1


ans1 = ans2 = 0
for a, b, prize in zip(a_list, b_list, prize_list):
    a_x, a_y = list(map(int, a))
    b_x, b_y = list(map(int, b))
    p_x, p_y = list(map(int, prize))

    # Part 1
    i = (p_x * b_y - b_x * p_y) / (a_x * b_y - b_x * a_y)
    j = (p_x * a_y - a_x * p_y) / (b_x * a_y - a_x * b_y)
    if (
        i == int(i)
        and j == int(j)
        and i * a_x + j * b_x == p_x
        and i * a_y + j * b_y == p_y
    ):
        ans1 += int(i * 3 + j)

    # Part 2
    p2_x, p2_y = p_x + 10000000000000, p_y + 10000000000000
    i = (p2_x * b_y - b_x * p2_y) / (a_x * b_y - b_x * a_y)
    j = (p2_x * a_y - a_x * p2_y) / (b_x * a_y - a_x * b_y)

    if (
        i == int(i)
        and j == int(j)
        and i * a_x + j * b_x == p2_x
        and i * a_y + j * b_y == p2_y
    ):
        ans2 += int(i * 3 + j)


print("Part 1:", ans1)
print("Part 2:", ans2)
