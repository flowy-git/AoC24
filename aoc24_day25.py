# setup
file = "./inputs/aoc24_day25_input.txt"
schematics = [[]]
locks = []
keys = []

# helper functions for part1
def divide_schems(schematics):
    for schem in schematics:
        if schem[0] == ['#', '#', '#', '#', '#']:
            lock = [schem[1], schem[2], schem[3], schem[4], schem[5]]
            locks.append(lock)
        else:
            key = [schem[1], schem[2], schem[3], schem[4], schem[5]]
            keys.append(key)

def schematic_to_heights(schems):
    toreturn = []
    for schem in schems:
        schem_h = []
        for i in range(5):
            count = 0
            for j in range(5):
                if schem[j][i] == '#':
                    count += 1
            schem_h.append(count)
        toreturn.append(schem_h)
    return toreturn

def overlaps(lock, key):
    for i in range(5):
        if lock[i] + key[i] > 5:
            return True
    return False

# defining part1
def part_1(schematics):
    toreturn = 0
    divide_schems(schematics)
    locks_h = schematic_to_heights(locks)
    keys_h = schematic_to_heights(keys)
    for lock in locks_h:
        for key in keys_h:
            if not overlaps(lock, key):
                toreturn += 1
    return toreturn

# load & process input
with open(file) as aoc_input:
    schematic_num = 0
    lock = True
    for line in aoc_input:
        if line == "\n":
            schematic_num += 1
            schematics.append([])
            continue
        line = line.replace("\n", "")
        line = list(line)
        schematics[schematic_num].append(line)
    part1 = part_1(schematics)

# print results
print("Part 1: ", part1)
#print("Part 2: ", part2)