# setup
file = "./inputs/aoc24_day6_input.txt"
maps = []


# general aid functions

def obstacle_infront(row, col, maps):
    guard = maps[row][col]
    if next_unmapped(row, col, maps):
        return False
    if guard == "^":
        if maps[row-1][col] !="#":
            return False
    elif guard == ">":
        if maps[row][col+1] !="#":
            return False
    elif guard == "<":
        if maps[row][col-1] !="#":
            return False
    elif guard == "v":
        if maps[row+1][col] !="#":
            return False
    return True

def next_unmapped(row, col, maps):
    guard = maps[row][col]
    if guard == "^":
        if row == 0:
            return True
    elif guard == ">":
        if col + 1 >= len(maps[row]):
            return True
    elif guard == "<":
        if col == 0:
            return True
    elif guard == "v":
        if row + 1 >= len(maps):
            return True
    return False

def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def part1(maps : list):
    visited = []
    symbols = ['^', '>', 'v', '<']
    guard_direction = 0
    guard_pos = [0,0]
    # find initial guard position
    #print('find startpos')
    for row in maps:
        for element in maps[maps.index(row)]:
            if element in symbols:
                guard_pos = [maps.index(row), row.index(element)]
    #print(guard_pos)
    #print('simulate')
    while True:
        #print(guard_pos)
        #print(maps[guard_pos[0]][guard_pos[1]])
        if [guard_pos[0],guard_pos[1]] not in visited:
            visited.append([guard_pos[0],guard_pos[1]])
            #print("added to visited")
        
        while True:
            if not obstacle_infront(guard_pos[0], guard_pos[1], maps):
                break
            guard_direction += 1
            maps[guard_pos[0]][guard_pos[1]] = symbols[guard_direction % 4]
        if [guard_pos[0],guard_pos[1]] not in visited:
            visited.append([guard_pos[0],guard_pos[1]])
        if next_unmapped(guard_pos[0], guard_pos[1], maps):
            #print("unmapped: ", guard_pos)
            break
        guard = maps[guard_pos[0]][guard_pos[1]]
        maps[guard_pos[0]][guard_pos[1]] = 'X'
        if guard == "^":
            guard_pos[0] -= 1
        elif guard == ">":
            guard_pos[1] += 1
        elif guard == "<":
            guard_pos[1] -= 1
        elif guard == "v":
            guard_pos[0] += 1
        maps[guard_pos[0]][guard_pos[1]] = guard
    #print('RETURN visited amount')
    #print(visited)
    return len(visited)
    

def part2(strings_list : list):
    counter = 0
    return counter

# load & process input
with open(file) as aoc_input:
    for line in aoc_input:
        line = line.replace("\n", "")
        line = list(line)
        maps.append(line)
    part1 = part1(maps)
    #part2 = part2(strings_list)
    #part2_result = part2(part2_string)

# print results
print("Part 1: ", part1)
#print("Part 2: ", part2)