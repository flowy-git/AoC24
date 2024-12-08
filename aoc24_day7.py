# setup
file = "./inputs/aoc24_day7_input.txt"
total_calibration_results = 0


def part1(results, values):
    toreturn = 0
    for i in range(len(results)):
        valid = False
        vals = values[i]
        num_ops = len(vals) - 1
        operators = ['#'] * num_ops
        print(operators)
        # we have LTR evaluation
        # so for each "operation" we have max 2 possible results
        # for n operations, we have 2**n possible results
        temporary_results = []
        for i in range(num_ops):
            temp_result1 = int(values[i]) + int(values[i+1])
            temp_result2 = int(values[i]) * int(values[i+1])
            temporary_results.append(temp_result1)
            temporary_results.append(temp_result2)
            


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
        print(line)
        line = line.split(':')
        results.append(int(line[0]))
        vals = line[1]
        vals = vals.split(' ')
        values.append(vals)
    part1_result = part1(results, values)


# print results
#print("Part 1: Reports safe: ", safe_count)
#print("Part 2: Reports safe with Problem Dampener: ", safe_damp_count)