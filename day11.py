from collections import deque
from itertools import combinations
import numpy as np

# Calculate shortest path between (startX, startY) and (endX, endY)
def shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    # Define set of valid directions, right, left, up , down
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque([(start, 0)])
    visited.add(start)

    while queue:
        (current, steps) = queue.popleft()
        if current == end:
            return steps

        for direction in directions:
            new_x = current[0] + direction[0]
            new_y = current[1] + direction[1]
            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] != 1 and (new_x, new_y) not in visited:
                queue.append(((new_x, new_y), steps + 1))
                visited.add((new_x, new_y))

    return -1  # If no path is found

# Replace all galexies with unique numbers
def replace_hashes_with_count(matrix):
    hash_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#':
                hash_count += 1
                matrix[i][j] = hash_count
            else:
                matrix[i][j] = 0

    return matrix, hash_count  # Return the modified array


#---------------------------------------------------------------------
# part 1
# Initialize an empty NumPy array
matrix = np.empty((0, 0)) 
num_steps = 0
with open('input_day11.txt', 'r') as f:
    for line in f.readlines():
        # build grid
        line = [list(line.strip())] 
        if matrix.size == 0:
            matrix = np.array(line)
        else:
            # append new rows
            matrix = np.vstack((matrix, line))
    
    expanded_matrix = matrix
    count = 0
    # Check for rows containing only '.' and insert a new row with '.' characters
    for i, row in enumerate(matrix):
        if np.all(row == '.'):
            count+=1
            new_row = np.full_like(row, '.', dtype='U')
            expanded_matrix = np.insert(expanded_matrix, count, new_row, axis=0)
        count +=1
            
    count = 0
    # Check for columns containing only '.' and insert a new column with '.' characters
    for i, col in enumerate(expanded_matrix.T):
        if np.all(col == '.'):
            count+=1
            new_col = np.full_like(col, '.', dtype='U')
            expanded_matrix = np.insert(expanded_matrix, count, new_col, axis=1)
        count+=1
    
    [expanded_matrix, hash_count] = replace_hashes_with_count(expanded_matrix.tolist())
    expanded_matrix = np.array(expanded_matrix)

    galexy_sets = list(combinations(list(range(1, hash_count + 1)), 2))


    for g_set in galexy_sets:
        print("Processing set: ", g_set[0], g_set[1])
        start = np.where(expanded_matrix == g_set[0])
        end = np.where(expanded_matrix == g_set[1])
        num_steps += shortest_path(expanded_matrix, (start[0][0], start[1][0]), (end[0][0], end[1][0]))  

    print(num_steps)

