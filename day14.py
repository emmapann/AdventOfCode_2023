import numpy as np

def get_load(matrix):
    south = matrix.shape[0]
    load = 0
    for i, row in enumerate(matrix):
        count = np.sum([word.count('O') for word in row])
        load += count*(south-i)
    return load

def move_O_north(matrix, start_row):
    for row in range(start_row, 0, -1):
        for i in range(matrix.shape[1]):
            if row > 0 and matrix[row][i] == 'O' and matrix[row-1][i] == '.':
                matrix[row][i], matrix[row-1][i] = matrix[row-1][i], matrix[row][i]
    if start_row + 1 == matrix.shape[0]:
        return matrix
    else:
        matrix = move_O_north(matrix, start_row+1)
    return matrix

def move_O_south(matrix, start_row):
    for row in range(0, start_row, 1):
        for i in range(matrix.shape[1]):
            if row < matrix.shape[0] and matrix[row][i] == 'O' and matrix[row+1][i] == '.':
                matrix[row][i], matrix[row+1][i] = matrix[row+1][i], matrix[row][i]
    if start_row - 1 == 0:
        return matrix
    else:
        matrix = move_O_south(matrix, start_row-1)
    return matrix

def move_O_east(matrix, start_col):
    for col in range(0, start_col, 1):
        for i in range(matrix.shape[0]):
            if col > 0 and matrix[i][col] == 'O' and matrix[i][col+1] == '.':
                matrix[i][col], matrix[i][col+1] = matrix[i][col+1], matrix[i][col]
    if start_col - 1 == 0:
        return matrix
    else:
        matrix = move_O_east(matrix, start_col-1)
    return matrix

def move_O_west(matrix, start_col):
    for col in range(start_col, 0, -1):
        for i in range(matrix.shape[0]):
            if col < matrix.shape[1] and matrix[i][col] == 'O' and matrix[i][col-1] == '.':
                matrix[i][col], matrix[i][col-1] = matrix[i][col-1], matrix[i][col]
    if start_col + 1 == matrix.shape[1]:
        return matrix
    else:
        matrix = move_O_west(matrix, start_col+1)
    return matrix

with open('input_day14_test.txt','r') as f:
    lines = f.readlines()

matrix = np.array([[char for char in line.strip()] for line in lines])
num_cycles = 1000000000
for i in range(0, int(num_cycles/4)):
    print(f"{i=}")
    matrix = move_O_north(matrix, 1)
    matrix = move_O_south(matrix, matrix.shape[0]-1)
    matrix = move_O_east(matrix, matrix.shape[1]-2)
    matrix = move_O_west(matrix, 1)

load = get_load(matrix)
print(f"{load=}")