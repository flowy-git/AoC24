# setup
import copy
file = "./inputs/aoc24_day18_input.txt"
coordinates = []

# coordinates are X;Y pairs
# X horizontal from left, Y vertical from top


# we start 0,0
# we want to get to exit := 70,70 (real input) bzw 6,6 (example input)

def part1(coordinates, num_bytes):

# load & process input
with open(file) as aoc_input:
    patterns_done = False
    for line in aoc_input:
        line = line.split(",")
        coordinates.append(line)
    part1 = part1(coordinates, 12)

# print results
print("Part 1: ", part1)
#print("Part 2: ", part2)