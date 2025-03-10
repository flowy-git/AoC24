# setup
file = "./inputs/aoc24_day13_input.txt"

# general aid functions

# load & process input
with open(file) as aoc_input:
    rules_done = False
    rules_list = []
    updates_list = []
    for line in aoc_input:
        line = line.replace("\n", "")
        if line == "":
            rules_done = True
            continue
        if not rules_done:
            line = line.split('|')
            rules_list.append(line)
        else:
            line = line.split(',')
            updates_list.append(line)
    #rules_dic = process_rules(rules_list)
    #part1_result = part1(updates_list, rules_dic)
    #part2_result = part2(updates_list, rules_dic)

# print results
#print("Part 1: ", part1_result)
#print("Part 2: ", part2_result)