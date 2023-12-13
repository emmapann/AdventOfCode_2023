import re
from itertools import product
import time
start_time = time.time()

# Find all groups containing consecutive '#' and '?' symbols
def find_consecutive_groups(input_string):
    pattern = r'[#?]+'
    return re.findall(pattern, input_string)

# Find all possible combinations if each '?' is replaced by a '.' OR '#'
# Example: .??..??...?##. 1,1,3
# This function breakes down into the following: 
#   1)  combos1=['..', '.#', '#.', '##']
#       hashes1=[[], [1], [1], [2]]
#
#   2)  combos2=['..', '.#', '#.', '##']
#       hashes2=[[], [1], [1], [2]]
#
#   3)  combos3=['.##', '###']
#       hashes3=[[2], [3]]
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

# Given the input target sequence, find all combinations that fulfill the target sequence in order
# Lists is generated from the function above
# Given the hashes examples above, this function picks an entry from each hashes list
# it validates by then seeing if the list matches the input target sequence
# Therefore, using the above example possible combos would be:
#   1) [hashes1[1], hashes2[1], hashes3[1]]
#   2) [hashes1[1], hashes2[2], hashes3[1]]
#   3) [hashes1[2], hashes2[1], hashes3[1]]
#   4) [hashes1[2], hashes2[2], hashes3[1]]
# This function returns all possible combos so the length of the ouput = 4 for this example
def find_combinations(lists, target_sequence):
    def check_sequence(combination):
        concatenated = [item for sublist in combination for item in sublist]
        return concatenated == target_sequence
    # Get all possible combinations
    possible_combinations = product(*lists)
    valid_combinations = []

    #TODO this part is the slow
    # For each possible combo, see if it fits the pattern for target sequence
    for combination in possible_combinations:
        #print("one combo")
        #print(f"{combination}")
        if check_sequence(combination):
            valid_combinations.append(combination)

    return valid_combinations if valid_combinations else None

#---------------------------------------------------------------------
# part 1
total = 0
with open('input_day12_test.txt', 'r') as f:
    for line in f.readlines():
        springs, rest = line.strip().split(' ')
        groups = find_consecutive_groups(springs)
        target_sequence = list(map(int, rest.split(',')))

        hash_groups = []
        for group in groups:
            combos, hashes = generate_combinations(group)
            print(f"{combos=}")
            print(f"{hashes=}")
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
# print("--- %s seconds ---" % (time.time() - start_time))





