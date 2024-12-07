# setup
import copy
file = "./inputs/aoc24_day6_input.txt"
mapped = []


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
    print(visited)
    return visited
    
def have_loop(start_pos, maps):
    visited = []
    symbols = ['^', '>', 'v', '<']
    guard_direction = 0
    guard_pos = start_pos[:]
    #print(guard_pos)
    while True:
        #print("checking for loop")
        
        if [guard_pos[0],guard_pos[1], symbols[guard_direction % 4]] in visited:
            #print("loop found:")
            #print(guard_pos[0],guard_pos[1], symbols[guard_direction % 4])
            #print(visited)
            return True
        else:
            visited.append([guard_pos[0],guard_pos[1], symbols[guard_direction % 4]])
        check_count = 0
        while True:
            check_count += 1
            if check_count > 5 or not obstacle_infront(guard_pos[0], guard_pos[1], maps):
                break
            guard_direction += 1
            maps[guard_pos[0]][guard_pos[1]] = symbols[guard_direction % 4]
        if next_unmapped(guard_pos[0], guard_pos[1], maps):
            #print("break unmapped")
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
    #print(visited)
    return False

def part2(maps, part1_visited):
    guard_pos = part1_visited[0]
    places= []
    part1_visited.pop(0)
    loop_count = 0
    #print("originalmap")
    #for line in maps:
        #print(line)
    for location in part1_visited:
        #print("locatio to check", location, "   ", guard_pos)
        mod_map = copy.deepcopy(maps)
        #print(guard_pos)
        mod_map[location[0]][location[1]] = '#'
        #print(guard_pos)
        if have_loop(guard_pos, mod_map):
            loop_count += 1
            places.append(location)
        #for line in mod_map:
        #    print(line)
        #print("location check done, guard pos: ", guard_pos)
    #for line in maps:
    #    print(line)
    print(places)
    return loop_count

    

# load & process input
with open(file) as aoc_input:
    for line in aoc_input:
        line = line.replace("\n", "")
        line = list(line)
        print(line)
        mapped.append(line)
    part1map = copy.deepcopy(mapped)
    part1 = part1(part1map)
    part1_result = len(part1)
    part2 = part2(mapped, part1)
    
    
    #part2_result = part2(part2_string)

# print results
print("Part 1: ", part1_result)
print("Part 2: ", part2)