import numpy as np

# Find indices of all the adjacent matching rows
def find_adjacent_pairs(numbers):
    pairs = []
    length = len(numbers)
    for i in range(length - 1):
        pairs.append([i, i + 1])
    return pairs

def find_matching_rc(np_matrix, shape, row):
    matching_set = []
    # Get correct dim
    if row:
        s = shape[0]
    else:
        s = shape[1]

    # Build up list of lists
    # matching_set contains all of the sets of matching row numbers
    # For example:
    # matching_set = [[0], [1, 3], [2], [4, 5]]
    # this means that the 0th and 2nd row are not repeated but rows 1 and 3
    # are equal and so are rows 4 and 5
    for row in np_matrix:
        curr_set = (np.where(np.all(np_matrix == row, axis=1))[0]).tolist()
        matching_set.append(curr_set)
    
    # Loop through the items in matching_set to try and find where the reflection point is
    for curr_set in matching_set:    
        l = len(curr_set)
        if l >= 2:
            # In order for there to be a reflection, first you need to find
            # an adjacent set of rows
            ind_list = find_adjacent_pairs(curr_set)
            for ind in ind_list:
                if (curr_set[ind[1]]-curr_set[ind[0]] == 1):
                    # Check if the other rows going out from this point also match...
                    for i in range(1, curr_set[ind[1]]+1):
                        search_set = [curr_set[ind[0]]-i, curr_set[ind[1]]+i]
                        if curr_set[ind[1]]+i < s and curr_set[ind[0]]-i >= 0:
                            # any two do not match, break, this cannot be the reflection poing
                            if not any(set(search_set).issubset(set(sublist)) for sublist in matching_set):
                                break
                        # If you have hit the last row or the first row, you know that you have 
                        # matched all of the reflections up to this point, you found the correct reflection
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
    # If the reflection was not in the rows, check the columns by transposing
    if not n:
        transposed_matrix = np_matrix.T
        n = find_matching_rc(transposed_matrix, shape, 0)
    num += n
print(f"{num}")
