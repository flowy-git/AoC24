# setup
file = "./inputs/aoc24_day23_input.txt"
connection = {}
threes = []

# PART1 FUNCTIONING
# PART2 - received tip on using bron-kerbosch algo - implementing pseudocode from wikipedia


# defining part1
def part1(connection):
    # get networks of three
    for key in connection.keys():
        set = connection[key]
        for i in set:
            for j in set:
                if i != j:
                    if j in connection[i] or i in connection[j]:
                        toappend = sorted([key, i, j])
                        if toappend not in threes:
                            threes.append(toappend)
    # filter for "t"
    toreturn = []
    for toappend in threes:
        append = False
        for computer in toappend:
            if computer[0] == 't':
                append = True
        if append:
            toreturn.append(toappend)
    return toreturn


# defining part2
def part2(connection, r=None, p=None, x=None, max_clique=None):
    if r is None:
        r = set()
        p = set(connection.keys())
        x = set()
        max_clique = []
    if not p and not x:
        if len(r) > len(max_clique):
            max_clique[:] = list(r)
        return

    pivot = None
    max_intersection = -1
    for u in p.union(x):
        intersection_size = len(p.intersection(set(connection[u])))
        if intersection_size > max_intersection:
            max_intersection = intersection_size
            pivot = u
    
    pivot_neighbors = set(connection[pivot]) if pivot else set()
    for v in p.difference(pivot_neighbors):
        neighbors_v = set(connection[v])
        part2(connection, r.union({v}), p.intersection(neighbors_v), x.intersection(neighbors_v), max_clique)
        p = p.difference({v})
        x = x.union({v})
    return max_clique

# load & process input
with open(file) as aoc_input:
    for line in aoc_input:
        line = line.replace("\n", "")
        line = line.split('-')
        if line[0] not in connection:
            connection[line[0]] = [line[1]]
        else:
            connection[line[0]].append(line[1])
        if line[1] not in connection:
            connection[line[1]] = [line[0]]
        else:
            connection[line[1]].append(line[0])
    part1 = len(part1(connection))
    part2_list = sorted(part2(connection))
    part2 = ""
    for node in part2_list:
        part2 += node
        part2 += ','
    part2 = part2[:-1]

# print results
print("Part 1: ", part1)
print("Part 2: ", part2)
