# setup
file = "./inputs/aoc24_day7_input.txt"


        # we have LTR evaluation
        # so for each "operation" we have max 2 possible results
        # for n operations, we have 2**n possible results
        # part1:
            # 0, 2(skip first two), 7(skip 1st 2, skip 2nd 4), 15(skip 1st 2, 2nd 4, 3rd 8)
        # part2:
            # basically raises up to 3**N
            # change accordingly



# Part1, essentially keep track of 2**n vals and in the end check 
def part1(results, values):
    toreturn = 0
    invalid_results = []
    invalid_vals = []
    for i in range(len(results)):
        vals = values[i]
        num_ops = len(vals) - 1

        temporary_results = []
        temp_result1 = int(vals[0]) + int(vals[1])
        temp_result2 = int(vals[0]) * int(vals[1])
        temporary_results.append(temp_result1)
        temporary_results.append(temp_result2)
        current_count = 0
        if len(vals) >= 2:
            for j in range(len(vals)-2):
                for test_case in temporary_results[current_count:]:
                    temp_result1 = test_case + int(vals[j+2])
                    temp_result2 = test_case * int(vals[j+2])
                    temporary_results.append(temp_result1)
                    temporary_results.append(temp_result2)
                current_count += 2**(j+1)
        if results[i] in temporary_results:
            toreturn += results[i]
        else:
            invalid_results.append(results[i])
            invalid_vals.append(vals)
    return invalid_results, invalid_vals, toreturn


#  Part2, basically part1, but we extend to n**3
def part2(results, values):
    toreturn = 0
    for i in range(len(results)):
        vals = values[i]
        num_ops = len(vals) - 1
        temporary_results = []
        temp_result1 = int(vals[0]) + int(vals[1])
        temp_result2 = int(vals[0]) * int(vals[1])
        temp_result3 = int(str(vals[0]) + str(vals[1]))
        temporary_results.append(temp_result1)
        temporary_results.append(temp_result2)
        temporary_results.append(temp_result3)
        current_count = 0
        if len(vals) >= 2:
            for j in range(len(vals)-2):
                for test_case in temporary_results[current_count:]:
                    temp_result1 = test_case + int(vals[j+2])
                    temp_result2 = test_case * int(vals[j+2])
                    temp_result3 = int(str(test_case) + str(vals[j+2]))
                    temporary_results.append(temp_result1)
                    temporary_results.append(temp_result2)
                    temporary_results.append(temp_result3)
                current_count += 3**(j+1)                    
        if results[i] in temporary_results:
            toreturn += results[i]
    return toreturn

# load & process input
with open(file) as aoc_input:
    results = []
    values = []
    for line in aoc_input:
        line = line.replace("\n", "")
        line = line.replace(": ", ":")
        line = line.split(':')
        results.append(int(line[0]))
        vals = line[1]
        vals = vals.split(' ')
        values.append(vals)
    part1_invalid_results, part1_invalid_vals,  part1_result = part1(results, values)
    part2_result = part1_result + part2(part1_invalid_results, part1_invalid_vals)
    # Optimisation measure recommended by someone -> have part2 only process the ones that are valid thru part2 problem change


# print results
print("Part 1: ", part1_result)
print("Part 2: ", part2_result)