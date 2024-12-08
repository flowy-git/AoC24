# setup
file = "./inputs/aoc24_day7_input.txt"
total_calibration_results = 0


def part1(results, values):
    toreturn = 0
    for i in range(len(results)):
        valid = False
        vals = values[i]
        num_ops = len(vals) - 1
        # we have LTR evaluation
        # so for each "operation" we have max 2 possible results
        # for n operations, we have 2**n possible results
        temporary_results = []
        temp_result1 = int(vals[0]) + int(vals[1])
        temp_result2 = int(vals[0]) * int(vals[1])
        temporary_results.append(temp_result1)
        temporary_results.append(temp_result2)
            # 0, 2(skip first two), 7(skip 1st 2, skip 2nd 4), 15(skip 1st 2, 2nd 4, 3rd 8),
        current_count = 0
        if len(vals) >= 2:
            for j in range(len(vals)-2):
                for test_case in temporary_results[current_count:]:
                    temp_result1 = test_case + int(vals[j+2])
                    temp_result2 = test_case * int(vals[j+2])
                    temporary_results.append(temp_result1)
                    temporary_results.append(temp_result2)
                current_count += 2**(j+1)
        #print(results[i])
        #print(temporary_results)
        if results[i] in temporary_results:
            toreturn += results[i]




        if valid:
            toreturn += results[i]

    return toreturn



# load & process input
with open(file) as aoc_input:
    results = []
    values = []
    for line in aoc_input:
        line = line.replace("\n", "")
        line = line.replace(": ", ":")
        #print(line)
        line = line.split(':')
        results.append(int(line[0]))
        vals = line[1]
        vals = vals.split(' ')
        values.append(vals)
    part1_result = part1(results, values)


# print results
print("Part 1: ", part1_result)
#print("Part 2: Reports safe with Problem Dampener: ", safe_damp_count)