import numpy as np
import math

def find_adjacent_pairs(numbers):
    pairs = []
    length = len(numbers)
    for i in range(length - 1):
        pairs.append([i, i + 1])
    return pairs

def find_matching_rc(np_matrix):
    found_match = False
    matching_set = []
    num = 0
    shape = np_matrix.shape

    # check for matching rows
    print("try rows")
    for row in np_matrix:
        curr_set = (np.where(np.all(np_matrix == row, axis=1))[0]).tolist()
        #print(f"{curr_set=}")
        matching_set.append(curr_set)
        #print(f"{matching_set=}")
    for curr_set in matching_set:    
        l = len(curr_set)
        if l >= 2:
            ind_list = find_adjacent_pairs(curr_set)
            for ind in ind_list:
                if (curr_set[ind[1]]-curr_set[ind[0]] == 1):
                    #print("reflection point: ", curr_set[ind[0]], curr_set[ind[1]])
                    # If the other rows going out from this point also match...
                    for i in range(1, curr_set[ind[1]]+1):
                        search_set = [curr_set[ind[0]]-i, curr_set[ind[1]]+i]
                        if curr_set[ind[1]]+i < shape[0] and curr_set[ind[0]]-i >= 0:
                            # any two do not match, break
                            if not any(set(search_set).issubset(set(sublist)) for sublist in matching_set):
                                #print("not found")
                                break
                            else:
                                pass
                                #print("found")
                        elif (search_set[1]==shape[1]-1 or search_set[0]<=0):
                                found_match = True
                                #print("found them all")
                                num = 100*curr_set[ind[1]]
                                break
                            
                    
    # check for matching cols, only if no reflective rows found
    matching_set = []
    if not found_match: 
        #print("try cols")
        transposed_matrix = np_matrix.T
        #print(f"{transposed_matrix}")
        # check for matching cols
        for col in transposed_matrix:
            #print(f"{col=}")
            curr_set = (np.where(np.all(transposed_matrix == col, axis=1))[0]).tolist()
            #print(f"{curr_set=}")
            matching_set.append(curr_set)
            #print(f"{matching_set=}")
        for curr_set in matching_set: 
            # If there are two rows next to each other that are the same, this could be the reflection point
            l = len(curr_set) 
            if l >= 2:
                ind_list = find_adjacent_pairs(curr_set)
                for ind in ind_list:
                    if (curr_set[ind[1]]-curr_set[ind[0]] == 1):
                        #print("reflection point: ", curr_set[ind[0]], curr_set[ind[1]])
                        # If the other rows going out from this point also match...
                        for i in range(1, curr_set[ind[1]]+1):
                            search_set = [curr_set[ind[0]]-i, curr_set[ind[1]]+i]
                            #print(f"{search_set=}")
                            if curr_set[ind[1]]+i < shape[1] and curr_set[ind[0]]-i >= 0:                        
                                if not any(set(search_set).issubset(set(sublist)) for sublist in matching_set):
                                    #print("not found")
                                    break
                                else:
                                    pass
                                    #print("found")
                            elif (search_set[1]==shape[1]-1 or search_set[0]<=0):
                                #print("found em all")
                                num = curr_set[ind[1]]
                                break
    return num

num = 0
with open('input_day13.txt', 'r') as f:
    file_content = f.read()

sections = [section.strip().split('\n') for section in file_content.split('\n\n')]
for section in sections:
    matrix = [line.split() for line in section]
    np_matrix = np.array([list(row) for sublist in matrix for row in sublist])
    n = find_matching_rc(np_matrix)
    print(n)
    num += n
print(f"{num}")

