# setup
import copy
file = "./inputs/aoc24_day19_input.txt"
patterns = []
designs = []

def next_step(verifying, design, pattern, solution):
    toreturn = [0]
    solution_found = False
    print("starting step")
    print(solution)
    print("ver : ", verifying)
    for poss_sol in solution:
        valid = False
        print("pos sol : ", poss_sol)
        if poss_sol != 0 and poss_sol[0] < poss_sol[1] and poss_sol[1] < len(verifying):
            temp_string = ""
            for i in poss_sol[2:]:
                temp_string += i
            if verifying[:poss_sol[1]+1] == temp_string[:poss_sol[1]+1]:
                poss_sol[0] = poss_sol[1]
                valid = True
            if temp_string == verifying:
                solution_found = True
                print("### SOLUTION FOUND ### ", verifying, "####")
        if not solution_found and valid:
            next_patt = []
            next_char = verifying[poss_sol[1]+1]
            for i in pattern:
                if i[:1] == next_char:
                    next_patt.append(i)
            for i in next_patt:
                new_poss_sol = copy.deepcopy(poss_sol)
                new_poss_sol.append(i)
                new_poss_sol[1] = new_poss_sol[1] + len(i)
                toreturn.append(new_poss_sol)
    print(toreturn)
    print("finished step")
    
    return toreturn, solution_found

def part1(pattern, design):
    number_possible = 0
    for check_design in design:
        print("checking : ", check_design)
        solution = [0]
        possible = False
        start = check_design[:1]
        print("start : ", start)
        for i in pattern:
            if i[:1] == start:
                solution.append([0, len(i) - 1, i])
        solution_found = False
        while True:
            if(solution[0] == 1) or len(solution) == 1 or solution_found:
                break
            solution, solution_found = next_step(check_design, design, pattern, solution)
        print(solution)
        if(possible):
            number_possible += 1
    return number_possible



# load & process input
with open(file) as aoc_input:
    patterns_done = False
    for line in aoc_input:
        if line != "\n" and not patterns_done:
            print(line)
            patterns_done = True
            line = line.replace("\n", "")
            line = line.split(", ")
            patterns = line
            continue
        elif line == "\n":
            continue
        line = line.replace("\n", "")
        print(line)
        designs.append(line)
    part1 = part1(patterns, designs)

# print results
print("Part 1: ", part1)
#print("Part 2: ", part2)