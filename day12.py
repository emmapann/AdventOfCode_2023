import re
from itertools import product
import time
start_time = time.time()

def find_consecutive_groups(input_string):
    pattern = r'[#?]+'
    return re.findall(pattern, input_string)

def generate_combinations(group):
    def count_contiguous_hashes(combination):
        counts = []
        count = 0
        for char in combination:
            if char == '#':
                count += 1
            else:
                if count > 0:
                    counts.append(count)
                count = 0
        if count > 0:
            counts.append(count)
        return counts

    def generate_helper(index, current):
        if index == len(group):
            combinations.append(current)
            contiguous_hashes.append(count_contiguous_hashes(current))
            return

        if group[index] == '?':
            generate_helper(index + 1, current + '.')
            generate_helper(index + 1, current + '#')
        else:
            generate_helper(index + 1, current + group[index])

    combinations = []
    contiguous_hashes = []
    generate_helper(0, '')

    return combinations, contiguous_hashes

def find_combinations(lists, target_sequence):
    def check_sequence(combination):
        concatenated = [item for sublist in combination for item in sublist]
        return concatenated == target_sequence
    possible_combinations = product(*lists)
    valid_combinations = []

    #TODO this part is the slow
    for combination in possible_combinations:
        #print("one combo")
        #print(f"{combination}")
        if check_sequence(combination):
            valid_combinations.append(combination)

    return valid_combinations if valid_combinations else None

#---------------------------------------------------------------------
# part 1
total = 0
with open('input_day12.txt', 'r') as f:
    for line in f.readlines():
        springs, rest = line.strip().split(' ')
        groups = find_consecutive_groups(springs)
        target_sequence = list(map(int, rest.split(',')))

        hash_groups = []
        for group in groups:
            combos, hashes = generate_combinations(group)
            hash_groups.append(hashes)

        selected_combinations = find_combinations(hash_groups, target_sequence)
        total += len(selected_combinations)
    print(total)
print("--- %s seconds ---" % (time.time() - start_time))


# #-----------------------------
# # part 2
# total = 0
# with open('input_day12_test.txt', 'r') as f:
#     for line in f.readlines():
#         springs, rest = line.strip().split(' ')
        
#         springs = (springs + "?") * (5) 
#         print(f"{springs=}")

#         target_sequence = list(map(int, rest.split(',')))
#         target_sequence = target_sequence * (5)
#         print(f"{target_sequence=}")
#         groups = find_consecutive_groups(springs)
#         #print(f"{groups=}")

#         hash_groups = []
#         for group in groups:
#             combos, hashes = generate_combinations(group)
#             hash_groups.append(hashes)
#             #print(f"{combos=}")
#             #print(f"{hashes=}")
#         #print(f"{hash_groups=}")
#         selected_combinations = find_combinations(hash_groups, target_sequence)
#         total += len(selected_combinations)
#     print(total)
#         #print(f"{selected_combinations=}")
#         #print(f"{len(selected_combinations)=}")





