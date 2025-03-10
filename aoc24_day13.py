# setup
file = "./inputs/aoc24_day13_input.txt"
import numpy as np
costA = 3
costB = 1
Machines = []
Machines_part2 = []

def part1_and_part2(Machines):
    num_prizes = 0
    total_tokens = 0
    for claw_machine in Machines:
        prize_won, token_cost = play_claw(claw_machine)
        if prize_won:
            num_prizes += 1
        total_tokens += token_cost
    return [num_prizes, total_tokens]

def play_claw(claw_machine):
    vals_A = claw_machine[0]
    vals_B = claw_machine[1]
    prize = claw_machine[2]
    solution_B = (( prize[0] / vals_A[0] ) - ( prize[1] / vals_A[1] )) / (( vals_B[0] / vals_A[0] ) - ( vals_B[1] / vals_A[1]))
    solution_A = ( prize[0] - ( solution_B * vals_B[0] )) / vals_A[0]
    round_A = round(solution_A)
    round_B = round(solution_B)
    if round_A*vals_A[0] + round_B*vals_B[0] == prize[0] and round_A*vals_A[1] + round_B*vals_B[1] == prize[1]:
        return True, (solution_A * costA + solution_B * costB)
    else:
        return False, 0

# load & process input
with open(file) as aoc_input:
    count = 0
    vals_A = ""
    vals_B = ""
    prize = ""
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
                line[1] = [value for value in line[1]]
                prize = line[1]
                Machines.append([vals_A, vals_B, prize])
                Machines_part2.append([vals_A, vals_B, [value+10000000000000 for value in prize]])
    part1_result = part1_and_part2(Machines)
    part2_result = part1_and_part2(Machines_part2)

# print results
print("Part 1: ", part1_result)
print("Part 2: ", part2_result)