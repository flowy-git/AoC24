# setup
file = "./inputs/aoc24_day10_input.txt"
import copy

# part1: want to find the sum of the scores of all trailheads
# step1: identify all trailheads -> starting from a zero, with slope of 1, to a 9, no diagonals
# step2: find all trails from the trailhead -> how many 9s can be reached from that single 0?
# step3: num(trails from trailhead) = score of trailhead, add to overall

# silly supporting functions
def value_of(values, pos):
    return values[pos[0]][pos[1]]

def diff_one(values, pos2, pos1):
    return values[pos1[0]][pos1[1]] - values[pos2[0]][pos2[1]] == 1

# function doing the heavy lifting for part1
def trailhead_score(values, trailhead_i, trailhead_j, origin, previous_pos = [0,0], depth = 0):
    #print("checking branch, depth: ", depth)
    pos = [trailhead_i, trailhead_j]
    previous_pos = previous_pos
    val = values[pos[0]][pos[1]]
        # set all possible next branches w/ diff of at most 1, remove the previous position
    next_possible_branches = []
    if pos[0] > 0 and diff_one(values, pos, [pos[0]-1, pos[1]]):
        next_possible_branches.append([pos[0]-1, pos[1]])
    if pos[0] < len(values) - 1 and diff_one(values, pos, [pos[0]+1, pos[1]]):
        next_possible_branches.append([pos[0]+1, pos[1]])
    if pos[1] > 0 and diff_one(values, pos, [pos[0], pos[1]-1]):
        next_possible_branches.append([pos[0], pos[1]-1])
    if pos[1] < len(values[pos[0]]) - 1 and diff_one(values, pos, [pos[0], pos[1]+1]):
        next_possible_branches.append([pos[0], pos[1]+1])
    next_possible_branches = [x for x in next_possible_branches if x not in [previous_pos]]
    nines_list = []
    #nines_count = 0
    if len(next_possible_branches) == 0 or depth > 10:
        return 0
    for branch_pos in next_possible_branches:
        if value_of(values, branch_pos) == 9:
            nines_list.append([origin, branch_pos])
        else:
            recursive = trailhead_score(values, branch_pos[0], branch_pos[1], origin, pos, (depth + 1))
            if recursive != 0:
                nines_list.extend(recursive)
    return nines_list

# function doing the heavy lifting for part2
def trailhead_rating(values, trailhead_i, trailhead_j, path, previous_pos = [0,0], depth = 0):
    pos = [trailhead_i, trailhead_j]
    previous_pos = previous_pos
    val = values[pos[0]][pos[1]]
    next_possible_branches = []
    if pos[0] > 0 and diff_one(values, pos, [pos[0]-1, pos[1]]):
        next_possible_branches.append([pos[0]-1, pos[1]])
    if pos[0] < len(values) - 1 and diff_one(values, pos, [pos[0]+1, pos[1]]):
        next_possible_branches.append([pos[0]+1, pos[1]])
    if pos[1] > 0 and diff_one(values, pos, [pos[0], pos[1]-1]):
        next_possible_branches.append([pos[0], pos[1]-1])
    if pos[1] < len(values[pos[0]]) - 1 and diff_one(values, pos, [pos[0], pos[1]+1]):
        next_possible_branches.append([pos[0], pos[1]+1])
    next_possible_branches = [x for x in next_possible_branches if x not in [previous_pos]]
    nines_list = []
    if len(next_possible_branches) == 0 or depth > 10:
        return 0
    for branch_pos in next_possible_branches:
        if value_of(values, branch_pos) == 9:
            newpath = copy.deepcopy(path)
            newpath.append(branch_pos)
            nines_list.append(newpath)
        else:
            newpath = copy.deepcopy(path)
            newpath.append(branch_pos)
            recursive = trailhead_rating(values, branch_pos[0], branch_pos[1], newpath, pos, (depth + 1))
            if recursive != 0:
                nines_list.extend(recursive)
    return nines_list

#part1
def part1(values):
    result_list = []
    toreturn = 0
    for i in range(len(values)):
        map_line = values[i]
        for j in range(len(map_line)):
            if map_line[j] == 0:
                nines_list = trailhead_score(values, i, j, [i,j])
                unique_list = []
                for a in nines_list:
                    if a not in unique_list:
                        unique_list.append(a)
                toreturn += len(unique_list)
                result_list.extend(unique_list)
    return toreturn

#part2
def part2(values):
    result_list = []
    toreturn = 0
    part1val = 0
    for i in range(len(values)):
        map_line = values[i]
        for j in range(len(map_line)):
            if map_line[j] == 0:
                path = [[i,j]]
                paths_list = trailhead_rating(values, i, j, path)
                unique_list = []
                for a in paths_list:
                    if a not in unique_list:
                        unique_list.append(a)
                toreturn += len(unique_list)
                result_list.extend(unique_list)
    return toreturn
    
# load & process input
with open(file) as aoc_input:
    values = []
    for line in aoc_input:
        line = line.replace("\n", "")
        line = line.replace(".", "1")
        line = [int(x) for x in line]
        values.append(line)
    part1_result = part1(values)
    part2_result, part1val = part2(values)

# print results
print("Part 1: ", part1_result)
print("Part 2: ", part2_result)