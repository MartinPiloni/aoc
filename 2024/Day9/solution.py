with open("day9.txt") as file:
    content = file.read()


even = True
id = 0
freq = []
freq_dots = []
disk = []
for num in content[:-1]:
    if even:
        disk.extend([id for _ in range(int(num))])
        freq.append(int(num))
        id += 1
    else:
        disk.extend([-1 for _ in range(int(num))])
        freq_dots.append(int(num))

    even ^= 1


# Save copy for part 2
freq2 = freq.copy()

# Part_1
fragmented_disk = []
id = len(freq) - 1
for c in disk:
    if c == -1 and id >= 0 and freq[id] > 0:
        freq[id] -= 1
        fragmented_disk.append(id)
        if freq[id] == 0:
            id -= 1
    elif c != "." and freq[c] > 0:
        freq[c] -= 1
        fragmented_disk.append(c)

ans1 = 0
for idx, c in enumerate(fragmented_disk):
    ans1 += c * idx

# Part 2 -- horrible solution
fragmented_disk2 = disk.copy()
for i in range(len(freq2) - 1, 0, -1):
    print(i)
    cnt = 0
    for j in range(len(fragmented_disk2)):
        if fragmented_disk2[j] == i:
            break

        if fragmented_disk2[j] == -1:
            cnt += 1
        else:
            cnt = 0

        if cnt == freq2[i]:
            for k in range(j + 1, len(fragmented_disk2)):
                if fragmented_disk2[k] == i:
                    fragmented_disk2[k] = -1

            for k in range(j - cnt + 1, j + 1):
                fragmented_disk2[k] = i

            break

ans2 = 0
for idx, c in enumerate(fragmented_disk2):
    if c != -1:
        ans2 += c * idx

print("Part 1:", ans1)
print("Part 2:", ans2)
