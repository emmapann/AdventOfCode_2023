# Advent of Code
# Day 1 


arr =  [3, 6, 7]
game_id, rest = arr.split(':')
_, id = game_id.strip().split(' ')
for set_colors in rest.strip().split(';'):
    pass



import re

#----------------------------------------------------------------------------------------
# part 1
calSum = 0
with open('input_day1.txt', 'r') as f:
    for line in f.readlines():
        #keep only numbers from the line
        numbers_only = re.sub(r'\D', '', line)
        if numbers_only:
            first_num = int(numbers_only[0])
            last_num = int(numbers_only[len(numbers_only)-1])
            calSum += (first_num * 10 + last_num)

print(calSum)

#----------------------------------------------------------------------------------------
# part 2

# List of substrings to find overlapping occurrences
substrings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# Create a dictionary mapping number words to their values
number_words_mapping = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

calSum = 0

for line in lines:
    # Find all integer matches in the string using regular expressions
    int_matches = re.finditer(r'\d', line)

    indices = [match.start() for match in int_matches]
    # get index of first integer
    first_int_index = indices[0] if indices else float('inf')
    # get index of last integer
    last_int_index = indices[-1] if indices else -1

    # Find the start index of the very first occurrence of any substring
    first_substring = None
    first_substring_index = float('inf')

    # Find the start index of the very last occurrence of any substring
    last_substring = None
    last_substring_index = -1

    for substring in substrings:
        matches = list(re.finditer(f'(?=({re.escape(substring)}))', line))
        if matches:
            # Retrieve the first occurrence
            if matches[0].start(1) < first_substring_index:
                first_substring = substring
                first_substring_index = matches[0].start(1)

            # Retrieve the last occurrence
            if matches[-1].start(1) > last_substring_index:
                last_substring = substring
                last_substring_index = matches[-1].start(1)

    # Get the first and last numbers
    first = number_words_mapping[first_substring] if (first_substring_index < first_int_index) else int(line[first_int_index])
    last = number_words_mapping[last_substring] if (last_substring_index > last_int_index) else int(line[last_int_index])

    calSum += (first * 10 + last)

print(calSum)