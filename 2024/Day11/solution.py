with open("day11.txt") as file:
    nums = list(map(int, file.read().split()))


# Copy for part 2
nums2 = nums.copy()

# Part 1
for _ in range(25):
    new_nums = []
    for num in nums:
        str_num = str(num)
        if num == 0:
            new_nums.append(1)
        elif len(str_num) % 2 == 0:
            new_nums.append(int(str_num[: len(str_num) // 2]))
            new_nums.append(int(str_num[len(str_num) // 2 :]))
        else:
            new_nums.append(num * 2024)

    nums = new_nums


ans1 = len(nums)

# Part 2
dp = {}


def calc(num, it):
    if it == 75:
        return 1

    if (num, it) in dp:
        return dp[(num, it)]

    str_num = str(num)
    if num == 0:
        dp[(num, it)] = calc(1, it + 1)
    elif len(str_num) % 2 == 0:
        dp[(num, it)] = calc(int(str_num[: len(str_num) // 2]), it + 1)
        dp[(num, it)] += calc(int(str_num[len(str_num) // 2 :]), it + 1)
    else:
        dp[(num, it)] = calc(num * 2024, it + 1)

    return dp[(num, it)]


ans2 = 0
for num in nums2:
    ans2 += calc(num, 0)

print("Part 1:", ans1)
print("Part 2:", ans2)
