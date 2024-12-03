# setup
import re
file = "./inputs/aoc24_day3_input.txt"
part1_string = ""
part2_string = ""

# general aid functions
def regex_pairs_to_values(regex_result_list : list) -> list:
    values_to_multiply = []
    for mult_pair in regex_result_list:
        vals_list = re.findall('\d+', mult_pair)
        int_vals_list = []
        for val in vals_list:
            int_vals_list.append(int(val))
        values_to_multiply.append(int_vals_list)
    return values_to_multiply

def multiply_vals(values_to_multiply : list) -> int:
    total = 0
    for pair in values_to_multiply:
        partial_sum = pair[0] * pair[1]
        total += partial_sum
    return total

# part 2 aid function
def part2_regex_extraction(part2_input : str) -> list:
    strings_to_process = []
    regex_results = []
    begin = re.search('^.*?(do\(\)|don\'t\(\))', part2_input)
    if begin:
        strings_to_process.append(begin.group())
    middle = re.findall('do\(\).*?don\'t\(\)', part2_input)
    if middle:
        strings_to_process.extend(middle)
    end = re.search('do\(\)(?!.*don\'t\(\)).*', part2_input)
    if end:
        strings_to_process.append(end.group())
    for segment in strings_to_process:
        regex_results.extend(re.findall('mul\(\d+,\d+\)', segment))
    return regex_results

# part1
def part1(part1_string):
    part1_regex_result_list = re.findall('mul\(\d+,\d+\)', part1_string)
    part1_vals_to_multiply = regex_pairs_to_values(part1_regex_result_list)
    part1_total = multiply_vals(part1_vals_to_multiply)
    return part1_total

# part2
def part2(part2_string):
    part2_regex_result_list = part2_regex_extraction(part2_string)
    part2_vals_to_multiply = regex_pairs_to_values(part2_regex_result_list)
    part2_total = multiply_vals(part2_vals_to_multiply)
    return part2_total

# load & process input
with open(file) as aoc_input:
    for line in aoc_input:
        line = line.replace("\n", "")
        part1_string += line
        part2_string += line
    part1_result = part1(part1_string)
    part2_result = part2(part2_string)

# print results
print("Part 1: ", part1_result)
print("Part 2: ", part2_result)