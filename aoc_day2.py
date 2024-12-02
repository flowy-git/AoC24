# setup
file = "aoc24_day2_input.txt"
safe_count = 0
safe_damp_count = 0

# aid functions

def desc_or_inc(report):
    descending = True
    increasing = True
    for i in range(len(report) - 1):
        if int(report[i]) > int(report[i+1]):
            descending = False
        if int(report[i]) < int(report[i+1]):
            increasing = False
    if descending or increasing:
        return True
    return False

def abs_diff(level1, level2):
    return abs(int(level1) - int(level2))
    
# Part 1 function
def report_safe(report):
    if not desc_or_inc(report):
        return False
    for i in range(len(report) - 1):
        if abs_diff(report[i], report[i+1]) not in [1,2,3]:
            return False
    return True

# Part 2 function - piggybacks off of Part 1
def damped_report_safe(report):
    if report_safe(report):
        return True
    else:
        safe = []
        for i in range(len(report)):
            level = report.pop(i)
            safe.append(report_safe(report))
            report.insert(i, level)
        return any(safe)

# load & process input
with open(file) as aoc_input:
    for line in aoc_input:
        line = line.replace("\n", "")
        line = line.split()
        
        # Part 1
        if report_safe(line):
            safe_count += 1
        
        # Part 2
        if damped_report_safe(line):
            safe_damp_count += 1




# print results
print("Part 1: Reports safe: ", safe_count)
print("Part 2: Reports safe with Problem Dampener: ", safe_damp_count)