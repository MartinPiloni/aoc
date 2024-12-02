ans1 = ans2 = 0


def is_safe(report):
    diffs = []
    for level, next_level in zip(report, report[1:]):
        diffs.append(level - next_level)

    if all((d > 0 and d <= 3) for d in diffs) or all(
        (d < 0 and d >= -3) for d in diffs
    ):
        return True


with open("./day2.txt") as file:
    for line in file:
        report = list(map(int, line.split()))
        if is_safe(report):
            ans1 += 1
            ans2 += 1
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i + 1 :]):
                    ans2 += 1
                    break

print("Part 1:", ans1)
print("Part 2:", ans2)
