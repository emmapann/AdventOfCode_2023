# Advent of Code
# Day 3
import re
import string


# #---------------------------------------------------------------------
# # part 1
# first_loop = True
# total = 0
# with open('input_day3.txt', 'r') as f:
#     lines = f.readlines()

#     # Get the current line and next lines
#     for current_line, next_line in zip(lines, lines[1:] + ['']):
#         current_line = current_line.strip()
#         next_line = next_line.strip()

#         # Find all numbers in the string and their start and end indices
#         matches = re.finditer(r'\d+', current_line)
    
#         # Get start and end indices of each number
#         curr_num_indices = [(match.start(), match.end() - 1) for match in matches]

#         # Find indices of symbols in CURRENT line
#         # Exclude the period
#         symbols = string.punctuation.replace('.', '')  
#         curr_symb_indices = [index for index, char in enumerate(current_line) if char in symbols]

#         # Find the same as above but for the NEXT line
#         next_symb_indices = [index for index, char in enumerate(next_line) if char in symbols]
#         for num in curr_num_indices:
#             adj_symb = False
#             # check adjacent positions as well as diagonals
#             # if current symbol is -1 from start or + 1 from end
#             for symb in curr_symb_indices:
#                 if (symb == num[0]-1 or symb == num[-1]+1):
#                     adj_symb = True
#                     break
#             # if next / prev symbol is -1 through + 1 from end
#             # If last iteration, do not check next line
#             for symb in next_symb_indices:
#                 if (num[0]-1 <= symb <= num[-1]+1):
#                     adj_symb = True
#                     break
#             # If first iteration, do not check prev line
#             if not(first_loop):
#                 for symb in prev_symb_indices:
#                     if (num[0]-1 <= symb <= num[-1]+1):
#                         adj_symb = True
#                         break
#             # If there is an adjacent symbol, add the number to the total output
#             if adj_symb:
#                 num_digits = num[-1] - num[0]
#                 noncum = 0
#                 for i in range(0, num_digits + 1):
#                     power = num_digits - i
#                     total += (int(current_line[num[0]+i]) * 10**(power))
#         first_loop = False
#         # Set previous values for next iteration
#         prev_symb_indices = curr_symb_indices

#     print(total)

#---------------------------------------------------------------------
# part 2
import re

def find_indices(content):
    number_indices = {}
    gear_indices = []

    for i, row in enumerate(content):
        matches = re.finditer(r'\d+', row)
        num_indices = [(match.start(), match.end() - 1) for match in matches]
        for start, end in num_indices:
            number = int(row[start:end + 1])
            if number in number_indices:
                number_indices[number].append(((i, start), (i, end)))
            else:
                number_indices[number] = [((i, start), (i, end))]

        gear_matches = [(m.start(), m.end() - 1) for m in re.finditer(r'\*', row)]
        gear_indices.extend([(i, start) for start, _ in gear_matches])

    return number_indices, gear_indices

# Function to find adjacent numbers to '*' and calculate product if there are 2 adjacent numbers
def calculate_adjacent_products(number_indices, gear_indices, content):
    total_products = 0
    for idx in gear_indices:
        i, j = idx
        adjacent_numbers = set()
        # Check above, below, left, right, and diagonal
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < len(content) and 0 <= new_j < len(content[new_i]):
                    for number, indices in number_indices.items():
                        for start_idx, end_idx in indices:
                            start_row, start_col = start_idx
                            end_row, end_col = end_idx
                            # If the index '*' is touching belongs to a number
                            if start_row <= new_i <= end_row and start_col <= new_j <= end_col:
                                adjacent_numbers.add(number)
        if len(adjacent_numbers) == 2:
            product = 1
            for num in adjacent_numbers:
                product *= num
            total_products += product

    return total_products


with open('input_day3.txt', 'r') as f:
    rows = f.read().strip().split('\n')

    # Get the start and end index pairs for each number
    number_indices, gear_indices = find_indices(rows)

    result = calculate_adjacent_products(number_indices, gear_indices, rows)
    print(f"Total product of adjacent numbers around '*': {result}")