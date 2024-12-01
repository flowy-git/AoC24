# setup
file = "aoc24_day1_input.txt"
list1 = []
list2 = []
distance = 0
similarity_score = 0

# load & process input
with open(file) as aoc_input:
    for line in aoc_input:
        line = line.replace("\n", "")
        line = line.split()
        list1.append(int(line[0]))
        list2.append(int(line[1]))

# part 1
list1.sort()
list2.sort()
for i in range(len(list1)):
    distance +=  abs(list1[i] - list2[i])

# part 2
for i in list1:
    occurrences = list2.count(i)
    similarity_score += i * occurrences

# print results
print("Part 1:", distance)
print("Part 2:", similarity_score)