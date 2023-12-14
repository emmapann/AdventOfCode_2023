import numpy as np

def find_adjacent_pairs(numbers):
    pairs = []
    length = len(numbers)
    for i in range(length - 1):
        pairs.append([i, i + 1])
    return pairs

def find_matching_rc(np_matrix, shape, row):
    matching_set = []
    if row:
        s = shape[0]
    else:
        s = shape[1]

    for row in np_matrix:
        curr_set = (np.where(np.all(np_matrix == row, axis=1))[0]).tolist()
        matching_set.append(curr_set)
        print(f"{matching_set=}")
    for curr_set in matching_set:    
        l = len(curr_set)
        if l >= 2:
            ind_list = find_adjacent_pairs(curr_set)
            for ind in ind_list:
                if (curr_set[ind[1]]-curr_set[ind[0]] == 1):
                    # If the other rows going out from this point also match...
                    for i in range(1, curr_set[ind[1]]+1):
                        search_set = [curr_set[ind[0]]-i, curr_set[ind[1]]+i]
                        if curr_set[ind[1]]+i < s and curr_set[ind[0]]-i >= 0:
                            # any two do not match, break
                            if not any(set(search_set).issubset(set(sublist)) for sublist in matching_set):
                                break
                        elif (search_set[1]==shape[1]-1 or search_set[0]<=0):
                                return curr_set[ind[1]]
    return []

num = 0
with open('input_day13.txt', 'r') as f:
    file_content = f.read()

sections = [section.strip().split('\n') for section in file_content.split('\n\n')]
for section in sections:
    matrix = [line.split() for line in section]
    np_matrix = np.array([list(row) for sublist in matrix for row in sublist])
    shape = np_matrix.shape
    n = 100 * find_matching_rc(np_matrix, shape, 1)
    if not n:
        transposed_matrix = np_matrix.T
        n = find_matching_rc(transposed_matrix, shape, 0)
    print(n)
    num += n
print(f"{num}")

