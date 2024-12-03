# setup
import re
file = "./inputs/aoc24_day3_input.txt"
regex_result_list = []
values_to_multiply = []
part2_string = ""
part2_do_mul_strings = []
part2_regex_result_list = []
part2_values_to_multiply = []
part2_total_sum = 0
part1_total_sum = 0

# TO-DO : reqrite to use functions -> want to reuse part1 efficiently for part2

# load & process input
with open(file) as aoc_input:
    for line in aoc_input:
        line = line.replace("\n", "")
        #extract valid mul using regex extraction
        regex_result_list.extend(re.findall('mul\(\d+,\d+\)', line))
        part2_string += line
        #part2_do_mul_strings.extend(re.findall('',line))

   
# process regex results to numerics : mul(\d+, \d+) -> [d,d]
for mult_pair in regex_result_list:
    vals_list = re.findall('\d+', mult_pair)
    int_vals_list = []
    for val in vals_list:
        int_vals_list.append(int(val))
    values_to_multiply.append(int_vals_list)

# multiply/evaluate the numerics : [d,d] -> d*d -> total += d*d
for pair in values_to_multiply:
    #print(pair)
    partial_sum = pair[0] * pair[1]
    #print(partial_sum)
    part1_total_sum += partial_sum

# part2: only take substrings with do(), none with don't(), and beginning is considered valid
# idea: extract the valid substrings, then run them through part1

part2_do_mul_strings.append(re.search('^.*?do', part2_string).group())
print(re.search('^.*?do', part2_string).group())
part2_do_mul_strings.extend(re.findall('do\(\).*don\'t\(\)', part2_string))
part2_do_mul_strings.append(re.search('do(?!.*do).*', part2_string).group())
print()
print(re.search('do(?!.*do).*', part2_string).group())

for line in part2_do_mul_strings:
    #print(line)
    part2_regex_result_list.extend(re.findall('mul\(\d+,\d+\)', line))

for mult_pair in part2_regex_result_list:
    vals_list = re.findall('\d+', mult_pair)
    int_vals_list = []
    for val in vals_list:
        int_vals_list.append(int(val))
    part2_values_to_multiply.append(int_vals_list)

# multiply/evaluate the numerics : [d,d] -> d*d -> total += d*d
for pair in part2_values_to_multiply:
    #print(pair)
    partial_sum = pair[0] * pair[1]
    #print(partial_sum)
    part2_total_sum += partial_sum

# print results
print("Part 1: ", part1_total_sum)
print("Part 2: ", part2_total_sum)