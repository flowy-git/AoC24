# setup
file = "./inputs/aoc24_day13_input.txt"
costA = 3
costB = 1
Machines = []
# general aid functions


# load & process input
with open(file) as aoc_input:
    count = 0
    vals_A = ""
    vals_B = ""
    prize = ""
    rules_list = []
    updates_list = []
    for line in aoc_input:
        count += 1
        line = line.replace("\n", "")
        line = line.replace(" ", "")
        line = line.replace("X", "")
        line = line.replace("Y", "")
        line = line.replace("+", "")
        line = line.replace("=", "")
        if line == "":
            continue
        else:
            line = line.split(':')
            line = [line[0], line[1].split(',')]
            line[1] = [int(value) for value in line[1]]
            if line[0] == "ButtonA":
                vals_A = line[1]
            elif line[0] == "ButtonB":
                vals_B = line[1]
            elif line[0] == "Prize":
                prize = line[1]
        if count % 3 == 0:
            Machines.append([vals_A, vals_B, prize])        

# print results
#print("Part 1: ", part1_result)
#print("Part 2: ", part2_result)
for line in Machines:
    print(line)