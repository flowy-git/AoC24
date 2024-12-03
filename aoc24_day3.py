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

# TO-DO : reqrite to use functions -> want to reuse part1 efficiently for part2

# load & process input
with open(file) as aoc_input:
    for line in aoc_input:
        line = line.replace("\n", "")
        regex_result_list.extend(re.findall('mul\(\d+,\d+\)', line))
        part1_vals_to_multiply = regex_pairs_to_values(regex_result_list)
        part1_total = multiply_vals(part1_vals_to_multiply)
        part2_string += line

# part2: only take substrings with do(), none with don't(), and beginning is considered valid
# idea: extract the valid substrings, then run them through part1
print('begin:')
begin = re.search('^.*?(do\(\)|don\'t\(\))', part2_string)
if begin:
    print(begin.group())
    part2_do_mul_strings.append(begin.group())

print('middle:')
middle = re.findall('do\(\).*?don\'t\(\)', part2_string)
if middle:
    for i in middle:
        print(i)
    part2_do_mul_strings.extend(middle)

    # OKAY SO I THINK I KNOW WHAT THE ISSUE IS
        # basically, when we do cutoffs by do() .... dont()
        # that is technically correct
        # but, it can create issues when the last part of the input doesn't have a dont()
        # now, I thought that would be fixed by having the last do() until the end $
        # but, that doesnt factor in a do() .... do() .... $ situation
    # possible fix:
        # rather than cutting off by do() .... dont(), we cut off by do() ... do() and do() ... dont()
        # using non-greedy!
        # YEAH FUCK NO THAT DIDNT WORK LMAO
    # new idea: keep middle the same, but adapt the end to not only go off of the last do(), but the last do() such that there is no more dont()

end = re.search('do\(\)(?!.*don\'t\(\)).*', part2_string)
print('end:')
if end:
    print(end.group())
    part2_do_mul_strings.append(end.group())

print()
#print("all extracted lines:")

for line in part2_do_mul_strings:
    #print(line)
    part2_regex_result_list.extend(re.findall('mul\(\d+,\d+\)', line))
print()
print("extracted mult pairs:")
for mult_pair in part2_regex_result_list:
    #print(mult_pair)
    vals_list = re.findall('\d+', mult_pair)
    #print(vals_list)
    int_vals_list = []
    for val in vals_list:
        int_vals_list.append(int(val))
    part2_values_to_multiply.append(int_vals_list)

# multiply/evaluate the numerics : [d,d] -> d*d -> total += d*d
for pair in part2_values_to_multiply:
    #print('pair to multiply')
    #print(pair)
    partial_sum = pair[0] * pair[1]
    #print(partial_sum)
    part2_total_sum += partial_sum

# print results
print("Part 1: ", part1_total)
print("Part 2: ", part2_total_sum)

# current solution is off by 1,696,277 (when comparing to shared solution)