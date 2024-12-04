# setup

file = "./inputs/aoc24_day4_input.txt"
strings_list = []
part1_xmas_counter = 0
part2_xmas_counter = 0


# general aid functions

def grab_surrounding_chars(row, col, strings_list):
    surrounding_chars_list = []
    for i in [row, row+1]:
        for j in [col, col+1]:
            if i < len(strings_list) and (j < len(strings_list[i])):
                surrounding_chars_list.append([i,j])
    return surrounding_chars_list

def valid_next_trim(row, col, next_chars_list, strings_list):
    valid_chars = []
    if strings_list[row][col] == 'X':
        valid = 'M'
    elif strings_list[row][col] == 'S':
        valid = 'A'
    for char_pos in next_chars_list:
        if strings_list[char_pos[0]][char_pos[1]] == valid:
            valid_chars.append(char_pos)
    return valid_chars

def check_last_two(row, col, char_2_pos, strings_list):
    row_increment = char_2_pos[0] - row
    col_increment = char_2_pos[1] - col
    if char_2_pos[0] + row_increment + row_increment < len(strings_list):
        if char_2_pos[1] + col_increment + col_increment < len(strings_list[char_2_pos[0]]):
            char_3_pos = [char_2_pos[0] + row_increment, char_2_pos[1] + col_increment]
            char_4_pos = [char_3_pos[0] + row_increment, char_3_pos[1] + col_increment]
            list_of_chars = []
            list_of_chars.append(strings_list[row][col])
            list_of_chars.append(strings_list[char_2_pos[0]][char_2_pos[1]])
            list_of_chars.append(strings_list[char_3_pos[0]][char_3_pos[1]])
            list_of_chars.append(strings_list[char_4_pos[0]][char_4_pos[1]])
            if list_of_chars == ['X', 'M', 'A', 'S']:
                return True
    return False

pos_list = []

def check_if_word(row, col, strings_list):
    word_count = 0 #between 0 and 3
    wrd1 = ['X', 'M', 'A', 'S']
    wrd2 = ['S', 'A', 'M', 'X']
    #word 1 horizontal
    if col + 3 < len(strings_list[row]):
        word = [strings_list[row][col], strings_list[row][col+1], strings_list[row][col+2], strings_list[row][col+3]]
        if word == wrd1 or word == wrd2:
            word_count += 1
            pos_list.append([row,col])
            pos_list.append([row,col+1])
            pos_list.append([row,col+2])
            pos_list.append([row,col+3])
    # word 2 vertical
    if row + 3 < len(strings_list):
        word = [strings_list[row][col], strings_list[row+1][col], strings_list[row+2][col], strings_list[row+3][col]]
        if word == wrd1 or word == wrd2:
            word_count += 1
            pos_list.append([row,col])
            pos_list.append([row+1,col])
            pos_list.append([row+2,col])
            pos_list.append([row+3,col])
    if row + 3 < len(strings_list) and col + 3 < len(strings_list[row]):
        word = [strings_list[row][col], strings_list[row+1][col+1], strings_list[row+2][col+2], strings_list[row+3][col+3]]
        if word == wrd1 or word == wrd2:
            word_count += 1
            pos_list.append([row,col])
            pos_list.append([row+1,col+1])
            pos_list.append([row+2,col+2])
            pos_list.append([row+3,col+3])
    if row + 3 < len(strings_list) and col - 3 >= 0:
        word = [strings_list[row][col], strings_list[row+1][col-1], strings_list[row+2][col-2], strings_list[row+3][col-3]]
        if word == wrd1 or word == wrd2:
            word_count += 1
            pos_list.append([row,col])
            pos_list.append([row+1,col-1])
            pos_list.append([row+2,col-2])
            pos_list.append([row+3,col-3])

    return word_count

def display_dump(strings_list):
    str_list = []
    for row_i in range(len(strings_list)):
        str1 = ""
        for col_j in range(len(strings_list[row_i])):
            if [row_i, col_j] in pos_list:
                str1 = str1 + strings_list[row_i][col_j]
            else:
                str1 = str1 + "."
        str_list.append(str1)
    for row_i in str_list:
        print(row_i)

def part1(strings_list : list):
    counter = 0
    for row_i in range(len(strings_list)):
        for col_j in range(len(strings_list[row_i])):
            if strings_list[row_i][col_j] == 'X' or strings_list[row_i][col_j] == 'S':
                counter += check_if_word(row_i, col_j, strings_list)
    #display_dump(strings_list)
    return counter

def check_if_x(row, col, strings_list):
    if row + 2 >= len(strings_list):
        return False
    if col + 2 >= len(strings_list[row]):
        return False
    if strings_list[row+1][col+1] != 'A':
        return False
    if (strings_list[row][col+2] != 'S') and (strings_list[row][col+2] != 'M'):
        return False
    if strings_list[row][col] == 'S':
        if strings_list[row+2][col+2] != 'M':
            return False
    if strings_list[row][col] == 'M':
        if strings_list[row+2][col+2] != 'S':
            return False
    if strings_list[row][col+2] == 'S':
        if strings_list[row+2][col] != 'M':
            return False
    if strings_list[row][col+2] == 'M':
        if strings_list[row+2][col] != 'S':
            return False
    return True

def part2(strings_list : list):
    counter = 0
    for row_i in range(len(strings_list)):
        for col_j in range(len(strings_list[row_i])):
            if strings_list[row_i][col_j] == 'M' or strings_list[row_i][col_j] == 'S':
                if check_if_x(row_i, col_j, strings_list):
                    counter += 1
    #display_dump(strings_list)
    return counter

# load & process input
with open(file) as aoc_input:
    for line in aoc_input:
        line = line.replace("\n", "")
        strings_list.append(line)
        #part2_string += line
    part1_xmas_counter = part1(strings_list)
    part2_xmas_counter = part2(strings_list)
    #part2_result = part2(part2_string)

# print results
print("Part 1: ", part1_xmas_counter)
print("Part 2: ", part2_xmas_counter)