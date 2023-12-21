import numpy as np
from scipy import ndimage

# Loop to check and append until the desired index exists in matrix
def ensure_index_existence(matrix, desired_index):
    #print(f"{desired_index=}")
    while True:
        # Check if the desired index is within the array's shape
        if (0 <= desired_index[0] < matrix.shape[0]) and (0 <= desired_index[1] < matrix.shape[1]):
            break  # Break the loop since the desired index exists
        else:
            # Append a new row or column depending on the index to accommodate the desired index
            if desired_index[0] >= matrix.shape[0]:
                # Append a row
                new_row = np.zeros((1, matrix.shape[1]), dtype=matrix.dtype)
                matrix = np.concatenate((matrix, new_row), axis=0)
            elif desired_index[1] >= matrix.shape[1]:
                # Append a column
                new_col = np.zeros((matrix.shape[0], 1), dtype=matrix.dtype)
                matrix = np.concatenate((matrix, new_col), axis=1)
            elif desired_index[0] < 0:
                # Append rows above
                deficit_rows = abs(desired_index[0])
                new_rows = np.zeros((deficit_rows, matrix.shape[1]), dtype=matrix.dtype)
                matrix = np.concatenate((new_rows, matrix), axis=0)
                curr_ind[0] -= desired_index[0]
                desired_index[0] = 0
            elif desired_index[1] < 0:
                # Append columns to the left
                deficit_cols = abs(desired_index[1])
                new_cols = np.zeros((matrix.shape[0], deficit_cols), dtype=matrix.dtype)
                matrix = np.concatenate((new_cols, matrix), axis=1)
                curr_ind[1] -= desired_index[1]
                desired_index[1] = 0
            else:
                break
            
    return matrix, desired_index, curr_ind

dig_plan = np.array([['#'], ['.']])
curr_ind = [0, 0]
part2 = True

with open('input_day18_test.txt', 'r') as f:
    for line in f.readlines():
        dir, meters, color = line.split(' ')
        meters = int(meters)
        print(f"{color=}")
        
        # For part 2, use color to get the dir and meters
        if (part2):
            meters = int(color[2:7], 16)
            print(f"{color[2:7]=}")
            print(f"{meters=}")
            dir = color[7]
            print(f"{dir=}")
            if dir == '0': dir = "R"
            elif dir == '1': dir = "D"
            elif dir == '2': dir = "L"
            else: dir = "U"
        
        match dir:
            case "R":
                next_ind = [curr_ind[0], curr_ind[1] + meters]
                # Check if there is room in the matrix to dig, if not make it larger
                if (next_ind[0] < dig_plan.shape[0]) and (next_ind[1] < dig_plan.shape[1]):
                    pass
                else:
                    dig_plan, _, _ = ensure_index_existence(dig_plan, next_ind)
                # From the current index to next index, add '#'
                for i in range(next_ind[1] - curr_ind[1]+1):
                    dig_plan[curr_ind[0]][curr_ind[1]+i] = '#'
                    
            case "L":
                next_ind = [curr_ind[0], curr_ind[1] - meters]
                # Check if there is room in the matrix to dig, if not make it larger
                if (next_ind[0] < dig_plan.shape[0]) and (next_ind[1] > 0):
                    pass
                else:
                    dig_plan, _, _ = ensure_index_existence(dig_plan, next_ind)
                if next_ind[1] < 0: next_ind[1] == 0
                # From the current index to next index, add '#'
                for i in range(curr_ind[1] - next_ind[1]+1):
                    dig_plan[curr_ind[0]][curr_ind[1]-i] = '#'

            case "D":
                next_ind = [curr_ind[0] + meters, curr_ind[1]]
                # Check if there is room in the matrix to dig, if not make it larger
                if (next_ind[0] < dig_plan.shape[0]) and (next_ind[1] < dig_plan.shape[1]):
                    pass
                else:
                    dig_plan, next_ind, curr_ind = ensure_index_existence(dig_plan, next_ind)
                # From the current index to next index, add '#'
                for i in range(next_ind[0] - curr_ind[0]+1):
                    dig_plan[curr_ind[0]+i][curr_ind[1]] = '#'

            case "U":
                next_ind = [curr_ind[0] - meters, curr_ind[1]]
                # Check if there is room in the matrix to dig, if not make it larger
                if (next_ind[0] > 0) and (next_ind[1] < dig_plan.shape[1]):
                    pass
                else:
                    dig_plan, next_ind, curr_ind = ensure_index_existence(dig_plan, next_ind)
                if next_ind[0] < 0: next_ind[0] == 0
                # From the current index to next index, add '#'
                for i in range(curr_ind[0] - next_ind[0]+1):
                    dig_plan[curr_ind[0]-i][curr_ind[1]] = '#'
        
        curr_ind = next_ind
print("original matrix: ")
print(dig_plan)
filled_array = (dig_plan == '#').astype(int)
filled_inside = ndimage.binary_fill_holes(filled_array).astype(int)
result_array = np.where(filled_inside == 1, '#', '')
print(result_array)
filled_count = np.count_nonzero(result_array == '#')
print(filled_count)