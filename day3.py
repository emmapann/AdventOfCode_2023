# Advent of Code
# Day 3
import re
import string


#---------------------------------------------------------------------
# part 1
first_loop = True
last_loop = False
total = 0
with open('input_day3.txt', 'r') as f:
    lines = f.readlines()

    for current_line, next_line in zip(lines, lines[1:]):
        current_line = current_line.strip()
        next_line = next_line.strip()

        # Find all numbers in the string and start and end indices
        matches = re.finditer(r'\d+', current_line)
    
        # Get start and end indices of each number
        curr_num_indices = [(match.start(), match.end() - 1) for match in matches]

        # Find indices of symbols in CURRENT line
        # Exclude the period
        symbols = string.punctuation.replace('.', '')  
        curr_symb_indices = [index for index, char in enumerate(current_line) if char in symbols]

        # Find the same as above but for the NEXT line
        next_symb_indices = [index for index, char in enumerate(next_line) if char in symbols]
        for num in curr_num_indices:
            adj_symb = False
            # check adjacent positions as well as diagonals
            # if current symbol is -1 from start or + 1 from end
            for symb in curr_symb_indices:
                if (symb == num[0]-1 or symb == num[-1]+1):
                    adj_symb = True
                    break
            # if next / prev symbol is -1 through + 1 from end
            # If last iteration, do not check next line
            for symb in next_symb_indices:
                if (num[0]-1 <= symb <= num[-1]+1):
                    adj_symb = True
                    break
            # If first iteration, do not check prev line
            if not(first_loop):
                for symb in prev_symb_indices:
                    if (num[0]-1 <= symb <= num[-1]+1):
                        adj_symb = True
                        break
            # If there is an adjacent symbol, add the number to the total output
            if adj_symb:
                num_digits = num[-1] - num[0]
                noncum = 0
                for i in range(0, num_digits + 1):
                    power = num_digits - i
                    total += (int(current_line[num[0]+i]) * 10**(power))
        first_loop = False
        # Set previous values for next iteration
        prev_symb_indices = curr_symb_indices
    
    # handle the very last line
    last_line = lines[-1].strip()
    # Find all numbers in the string and start and end indices
    matches = re.finditer(r'\d+', last_line)
    # Get start and end indices of each number
    curr_num_indices = [(match.start(), match.end() - 1) for match in matches]

    # Find indices of symbols in CURRENT line
    # Exclude the period
    symbols = string.punctuation.replace('.', '')  
    curr_symb_indices = [index for index, char in enumerate(last_line) if char in symbols]
    for num in curr_num_indices:
            adj_symb = False
            # check adjacent positions as well as diagonals
            # if current symbol is -1 from start or + 1 from end
            for symb in curr_symb_indices:
                if (symb == num[0]-1 or symb == num[-1]+1):
                    adj_symb = True
                    break
            # If first iteration, do not check prev line
            for symb in prev_symb_indices:
                if (num[0]-1 <= symb <= num[-1]+1):
                    adj_symb = True
                    break
            # If there is an adjacent symbol, add the number to the total output
            if adj_symb:
                num_digits = num[-1] - num[0]
                noncum = 0
                for i in range(0, num_digits + 1):
                    power = num_digits - i
                    total += (int(last_line[num[0]+i]) * 10**(power))


    print(total)