def is_ordered(pages, graph):
    vis = {} for page in pages:
        vis[page] = True
        if page not in graph:
            continue

        for neighbor in graph[page]:
            if vis.get(neighbor):
                return False

    return True


def order(pages, graph):
    for i in range(len(pages)):
        for j in range(len(pages)):
            if pages[j] in graph[pages[i]]:
                pages[i], pages[j] = pages[j], pages[i]

    return pages


ans1 = ans2 = 0
with open("day5.txt") as file:
    rules = True
    unordered = []
    graph = {}
    for line in file:
        line = line.strip()
        if not len(line):
            rules = False
            continue

        if rules:
            a, b = line.split("|")
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]
        else:
            pages = line.split(",")
            if is_ordered(pages, graph):
                ans1 += int(pages[len(pages) // 2])
            else:
                pages = order(pages, graph)
                ans2 += int(pages[len(pages) // 2])

print("Part1:", ans1)
print("Part2:", ans2)
