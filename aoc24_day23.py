# setup
file = "./inputs/aoc24_day23_input.txt"
connection = {}
threes = []
# helper functions



# defining part1
def part1(connection):
    # get networks of three
    for key in connection.keys():
        #print(key)
        set = connection[key]
        #print(set)
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

# print results
print("Part 1: ", part1)
#print("Part 2: ", part2)
