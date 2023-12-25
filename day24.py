
#----------------------------------------
# part 1

# global x_max
# global x_min
# global y_max
# global y_min

# def count_intersections(positions, velocities):
#     total_count = 0

#     # Find the intersection point using formula
#     def calculate_intersection(p1, v1, p2, v2):
#         t = ((p2[0] - p1[0]) * v2[1] - (p2[1] - p1[1]) * v2[0]) / (v1[0] * v2[1] - v1[1] * v2[0])
#         return p1[0] + v1[0] * t, p1[1] + v1[1] * t

#     # Consider all combinations of lines
#     for i in range(len(positions)):
#         for j in range(i + 1, len(positions)):
#             pos1 = positions[i]
#             vel1 = velocities[i]
#             pos2 = positions[j]
#             vel2 = velocities[j]

#             x1, y1 = pos1
#             vx1, vy1 = vel1
#             x2, y2 = pos2
#             vx2, vy2 = vel2

#             # Check if one line vertical and one horizontal
#             if (vx1 == 0 and vy2 == 0) or (vy1 == 0 and vx2 == 0):
#                 total_count += 1
#                 continue  # Skip other intersection checks for this pair

#             # Check that lines are not parallel
#             if vx1 * vy2 - vy1 * vx2 != 0:
#                 intersection_x, intersection_y = calculate_intersection(pos1, vel1, pos2, vel2)

#             # Make sure moving in same direction so that they intersect in the 'future'
#                 if (
#                     x_min <= intersection_x <= x_max
#                     and y_min <= intersection_y <= y_max
#                     and ((vx1 > 0 and intersection_x >= x1) or (vx1 < 0 and intersection_x <= x1))
#                     and ((vy1 > 0 and intersection_y >= y1) or (vy1 < 0 and intersection_y <= y1))
#                     and ((vx2 > 0 and intersection_x >= x2) or (vx2 < 0 and intersection_x <= x2))
#                     and ((vy2 > 0 and intersection_y >= y2) or (vy2 < 0 and intersection_y <= y2))
#                 ):
#                     total_count += 1

#     return total_count

# positions = []
# velocities = []

# x_max = 400000000000000
# x_min = 200000000000000
# y_max = 400000000000000
# y_min = 200000000000000

# with open('input_day24.txt', 'r') as f:
#     for line in f.readlines():
#         pos, vel = line.strip().split('@')
#         pos = list(map(int, pos.split(',')))
#         positions.append((pos[0], pos[1]))
#         vel = list(map(int, vel.split(',')))
#         velocities.append((vel[0], vel[1]))

# num_intersections = count_intersections(positions, velocities)
# print(f"The number of intersections among trajectories is: {num_intersections}")

#--------------------------------------------
# part 2
# 
# Definitely had some help from AoC Reddit for ideas for this one
# Had to reach back into my brain for linear algebra
# 
# Main idea:
# Use some algebraic manipulation to reduce the number of unknowns / equations by having the 
# rock start at the same position as the first hailstone in the list at t=0
# 
# Result is linear system of 4 equations
# Use Cramer's Rule to solve: solution of a system of linear equations with as many equations as unknowns when there is a unique solution
#     x_pos_rock (y0_vel - y1_vel) + y_pos_rock (x1_vel - x0_vel) + x_vel_rock (y1_pos - y0_pos) + y_vel_rock (x0_pos - x1_pos) - x0_pos y0_vel + y0_pos x0_vel + x1_pos y1_vel - y1_pos x1_vel = 0
#     x_pos_rock (y2_vel - y3_vel) + y_pos_rock (x3_vel - x2_vel) + x_vel_rock (y3_pos - y2_pos) + y_vel_rock (x2_pos - x3_pos) - x2_pos y2_vel + y2_pos x2_vel + x3_pos y3_vel - y3_pos x3_vel = 0
#     x_pos_rock (y4_vel - y5_vel) + y_pos_rock (x5_vel - x4_vel) + x_vel_rock (y5_pos - y4_pos) + y_vel_rock (x4_pos - x5_pos) - x4_pos y4_vel + y4_pos x4_vel + x5_pos y5_vel - y5_pos x5_vel = 0
#     x_pos_rock (y6_vel - y7_vel) + y_pos_rock (x7_vel - x6_vel) + x_vel_rock (y7_pos - y6_pos) + y_vel_rock (x6_pos - x7_pos) - x6_pos y6_vel + y6_pos x6_vel + x7_pos y7_vel - y7_pos x7_vel = 0
#
# That gives us a nice linear system with four equations.  Cramer's rule (using integer math) takes care of it.
#
import numpy as np
import sympy as sp
start_positions = []
velocities = []

with open('input_day24.txt', 'r') as f:
    for line in f.readlines():
        pos, vel = line.strip().split('@')
        pos = list(map(int, pos.split(',')))
        start_positions.append((pos[0], pos[1], pos[2]))
        vel = list(map(int, vel.split(',')))
        velocities.append((vel[0], vel[1], vel[2]))

x0_pos, y0_pos, z0_pos = start_positions[0]
x0_vel, y0_vel, z0_vel = velocities[0]
x1_pos, y1_pos, z1_pos = start_positions[1]
x1_vel, y1_vel, z1_vel = velocities[1]
x2_pos, y2_pos, z2_pos = start_positions[2]
x2_vel, y2_vel, z2_vel = velocities[2]
x3_pos, y3_pos, z3_pos = start_positions[3]
x3_vel, y3_vel, z3_vel = velocities[3]
x4_pos, y4_pos, z4_pos = start_positions[4]
x4_vel, y4_vel, z4_vel = velocities[4]
x5_pos, y5_pos, z5_pos = start_positions[5]
x5_vel, y5_vel, z5_vel = velocities[5]
x6_pos, y6_pos, z6_pos = start_positions[6]
x6_vel, y6_vel, z6_vel = velocities[6]
x7_pos, y7_pos, z7_pos = start_positions[7]
x7_vel, y7_vel, z7_vel = velocities[7]

A = sp.Matrix([[ y0_vel - y1_vel, x1_vel - x0_vel, y1_pos - y0_pos, x0_pos - x1_pos],
              [ y2_vel - y3_vel, x3_vel - x2_vel, y3_pos - y2_pos, x2_pos - x3_pos],
              [ y4_vel - y5_vel, x5_vel - x4_vel, y5_pos - y4_pos, x4_pos - x5_pos],
              [ y6_vel - y7_vel, x7_vel - x6_vel, y7_pos - y6_pos, x6_pos - x7_pos]])

b = sp.Matrix([[ x0_pos * y0_vel - y0_pos * x0_vel + y1_pos * x1_vel - x1_pos * y1_vel],
              [ x2_pos * y2_vel - y2_pos * x2_vel + y3_pos * x3_vel - x3_pos * y3_vel],
              [ x4_pos * y4_vel - y4_pos * x4_vel + y5_pos * x5_vel - x5_pos * y5_vel],
              [ x6_pos * y6_vel - y6_pos * x6_vel + y7_pos * x7_vel - x7_pos * y7_vel]])

# I tried using Numpy's built-in determinant function, but that gave me the wrong answer
# After doing some reading on the AoC Reddit and some research on Numpy's implementation,
# I found that Numpy uses LU decomposition or other numerical methods. I looked up other 
# Python libraries that compute the determinant and found that SymPy might be a better option
# After I switched to SymPy, I got the correct solution.

detA = A.det()
print(f"{detA=}")
print("got det(A)")
A = A.reshape(1, A.shape[0]*A.shape[1]).tolist()[0]
print(f"{A=}")
b = b.reshape(1, b.shape[0]*b.shape[1]).tolist()[0]

# use // to round to int
x_pos_rock = (sp.Matrix( [[b[0], A[1], A[2], A[3]],
                [b[1], A[5], A[6], A[7]],
                [b[2], A[9], A[10], A[11]],
                [b[3], A[13], A[14], A[15]]]).det()) // detA

y_pos_rock = (sp.Matrix( [[A[0], b[0], A[2], A[3]],
                [A[4], b[1], A[6], A[7]],
                [A[8], b[2], A[10], A[11]],
                [A[12], b[3], A[14], A[15]]]) .det()) // detA

x_vel_rock = (sp.Matrix( [[A[0], A[1], b[0], A[3]],
                [A[4], A[5], b[1], A[7]],
                [A[8], A[9], b[2], A[11]],
                [A[12], A[13], b[3], A[15]]]).det()) // detA

y_vel_rock = (sp.Matrix( [[A[0], A[1], A[2], b[0]],
                [A[4], A[5], A[6], b[1]],
                [A[8], A[9], A[10], b[2]],
                [A[12], A[13], A[14], b[3]]]).det()) // detA


t0 = ( x_pos_rock - x0_pos ) // ( x0_vel - x_vel_rock )
print(f"{t0=}")
t1 = ( x_pos_rock - x1_pos ) // ( x1_vel - x_vel_rock )
print(f"{t1=}")
z_vel_rock = ( z0_pos - z1_pos + t0 * z0_vel - t1 * z1_vel ) // ( t0 - t1 )
print(f"{z_vel_rock=}")
z_pos_rock = z0_pos + t0 * ( z0_vel - z_vel_rock )
print(f"{z_pos_rock=}")

print( x_pos_rock + y_pos_rock + z_pos_rock )
