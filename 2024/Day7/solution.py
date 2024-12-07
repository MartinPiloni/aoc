ans1 = ans2 = 0
with open("day7.txt") as file:
    for line in file:
        result, nums = line.split(":")
        nums = list(map(int, nums.split()))

        # Part 1
        # Bitmask base 2 to generate all posible combinations of signs
        for mask in range(1 << (len(nums) - 1)):
            operators = []
            for j in range(len(nums) - 1):
                if mask & (1 << j):
                    operators.append("+")
                else:
                    operators.append("*")

            res = nums[0]
            for i in range(1, len(nums)):
                if operators[i - 1] == "+":
                    res += nums[i]
                else:
                    res *= nums[i]

            if res == int(result):
                ans1 += int(result)
                break

        # Part 1
        # Bitmask base 3 to generate all posible combinations of signs
        for mask in range(3 ** (len(nums) - 1)):
            operators = []
            for j in range(len(nums) - 1):
                if (mask // (3**j)) % 3 == 0:
                    operators.append("+")
                elif (mask // (3**j)) % 3 == 1:
                    operators.append("*")
                else:
                    operators.append("|")

            res = nums[0]
            for i in range(1, len(nums)):
                if operators[i - 1] == "+":
                    res += nums[i]
                elif operators[i - 1] == "*":
                    res *= nums[i]
                else:
                    res = int(str(res) + str(nums[i]))

            if res == int(result):
                ans2 += res
                break


print("Part 1:", ans1)
print("Part 2:", ans2)
