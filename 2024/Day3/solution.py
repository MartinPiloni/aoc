import re

ans1 = ans2 = 0
with open("day3.txt") as file:
    enabled = True
    for line in file:
        for a, b, do, dont in re.findall(
            r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line
        ):
            if do:
                enabled = True
            elif dont:
                enabled = False
            else:
                ans1 += int(a) * int(b)
                if enabled:
                    ans2 += int(a) * int(b)

print("Part 1:", ans1)
print("Part 2:", ans2)
