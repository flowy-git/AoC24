# setup
file = "./inputs/aoc24_day5_input.txt"

# general aid functions

def process_rules(rules_list):
    rules_dic = {}
    for rule_pair in rules_list:
        if rule_pair[0] in rules_dic:
            tmp_list = rules_dic[rule_pair[0]]
            tmp_list.append(rule_pair[1])
            rules_dic[rule_pair[0]] = tmp_list
        else:
            rules_dic[rule_pair[0]] = [rule_pair[1]] 
    return rules_dic

def valid_update(update, rules_dic):
    for i in range(len(update)):
        if update[i] in rules_dic:
            page_rules = rules_dic[update[i]]
            to_check = update[:i]
            for element in to_check:
                if element in page_rules:
                    return False
    return True

def reorder_update(update, rules_dic):
    for i in range(len(update)):
        relocate = []
        if update[i] in rules_dic:
            page_rules = rules_dic[update[i]]
            to_check = update[:i]
            for element in to_check:
                if element in page_rules:
                    relocate.append(element)
        for element in relocate:
            update.remove(element)
            update.insert(i, element)
    return update  

# part1
def part1(updates_list, rules_dic):
    middlesums = 0
    for update in updates_list:
        if valid_update(update, rules_dic):
            middlesums += int(update[(len(update)-1)//2])
    return middlesums
       
# part2
def part2(updates_list, rules_dic):
    middlesums = 0
    invalid_updates = []
    reordered_updates = []
    for update in updates_list:
        if not valid_update(update, rules_dic):
            reordered_updates.append(reorder_update(update, rules_dic))
    for update in reordered_updates:
        middle_page = update[(len(update)-1)//2]
        middlesums += int(middle_page)
    return middlesums

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
    rules_dic = process_rules(rules_list)
    part1_result = part1(updates_list, rules_dic)
    part2_result = part2(updates_list, rules_dic)

# print results
print("Part 1: ", part1_result)
print("Part 2: ", part2_result)