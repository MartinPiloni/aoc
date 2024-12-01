left = []
right = []
with open("day1_1.txt") as file:
    for line in file:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

left.sort()
right.sort()
ans1 = ans2 = 0
for v1, v2 in zip(left, right):
    ans1 += abs(v1 - v2)
    ans2 += v1 * right.count(v1)

print("Part 1:", ans1)
print("Part 2:", ans2)
