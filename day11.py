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

# Get updated indices using empty row / col knowledge
def get_indices_of_hash(matrix, empty_rows, empty_cols):
    indices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#':
                rows_to_add = 999999 * sum([i >= r for r in empty_rows])
                cols_to_add = 999999 * sum([j >= c for c in empty_cols])
                indices.append((i + rows_to_add, j + cols_to_add))
    return indices

# Calculate Manhattan distance between two points
def manhattan_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])


# #---------------------------------------------------------------------
# # part 1
# # Initialize an empty NumPy array
# matrix = np.empty((0, 0)) 
# num_steps = 0
# with open('input_day11.txt', 'r') as f:
#     for line in f.readlines():
#         # build grid
#         line = [list(line.strip())] 
#         if matrix.size == 0:
#             matrix = np.array(line)
#         else:
#             # append new rows
#             matrix = np.vstack((matrix, line))
    
#     expanded_matrix = matrix
#     count = 0
#     # Check for rows containing only '.' and insert a new row with '.' characters
#     for i, row in enumerate(matrix):
#         if np.all(row == '.'):
#             count+=1
#             new_row = np.full_like(row, '.', dtype='U')
#             expanded_matrix = np.insert(expanded_matrix, count, new_row, axis=0)
#         count +=1
            
#     count = 0
#     # Check for columns containing only '.' and insert a new column with '.' characters
#     for i, col in enumerate(expanded_matrix.T):
#         if np.all(col == '.'):
#             count+=1
#             new_col = np.full_like(col, '.', dtype='U')
#             expanded_matrix = np.insert(expanded_matrix, count, new_col, axis=1)
#         count+=1
    
#     [expanded_matrix, hash_count] = replace_hashes_with_count(expanded_matrix.tolist())
#     expanded_matrix = np.array(expanded_matrix)

#     galexy_sets = list(combinations(list(range(1, hash_count + 1)), 2))


#     for g_set in galexy_sets:
#         print("Processing set: ", g_set[0], g_set[1])
#         start = np.where(expanded_matrix == g_set[0])
#         end = np.where(expanded_matrix == g_set[1])
#         num_steps += shortest_path(expanded_matrix, (start[0][0], start[1][0]), (end[0][0], end[1][0]))  

#     print(num_steps)

#--------------------------------------------------------------------
# Part 2
# The implementation in part 1 works for a smaller sized matrix, but once I read that part 2 would require adding
# millions of rows and columns, I needed to rethink the strategy. Instead of doing BFS algorithm, can just use indices
# and use Manhattan Distance formula to find distance between two points. I will search the original input and keep 
# track of the 'empty' rows and columns. Then I will search the input to find the '#' and in the same function, calculate 
# the X and Y index of each '#' while applying the knowledge of where the empty rows and columns are. Once the updated
# indices are found, can use combinations and distance formula and add up all the distances to get total steps. 
    
# Initialize an empty NumPy array
matrix = np.empty((0, 0)) 
empty_rows = []
empty_cols = []

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
    
    # Check for rows containing only '.' and store info
    for i, row in enumerate(matrix):
        if np.all(row == '.'):
            empty_rows.append(i)
            
    # Check for columns containing only '.' and store info
    for i, col in enumerate(matrix.T):
        if np.all(col == '.'):
            empty_cols.append(i)

    # Get indices, taking into account where the empty rows / cols are
    indices = get_indices_of_hash(matrix, empty_rows, empty_cols)

    distances = []
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            distance = manhattan_distance(indices[i], indices[j])
            distances.append((indices[i], indices[j], distance))
            num_steps += distance
    print(num_steps)

