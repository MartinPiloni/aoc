import re

ROWS = 103
COLS = 101

ans1 = q1 = q2 = q3 = q4 = 0
with open("day14.txt") as file:
    for line in file:
        c, r, v_c, v_r = list(map(int, re.findall(r"-*\d+", line)))
        final_row = (r + v_r * 100) % ROWS
        final_col = (c + v_c * 100) % COLS

        if final_row == ROWS // 2 or final_col == COLS // 2:
            continue
        elif final_row < ROWS // 2 and final_col < COLS // 2:
            q1 += 1
        elif final_row < ROWS // 2 and final_col > COLS // 2:
            q2 += 1
        elif final_row > ROWS // 2 and final_col < COLS // 2:
            q3 += 1
        else:
            q4 += 1

    ans1 = q1 * q2 * q3 * q4

print("Part 1:", ans1)
