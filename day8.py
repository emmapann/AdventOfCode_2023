# Advent of code 2023
# day 8
from itertools import cycle
import math

# Build dict representing a tree-like structure
def build_tree(nodes):
    tree = {}
    for node in nodes:
        # node structure is root = (left, right)
        root, rest = node.split('=')
        root = root.replace(' ','')
        rest = rest.replace('(', '').replace(')', '')
        left, right = rest.strip().split(',')
        tree[root] = (left.strip(), right.strip())  # Store left and right connections for each node
    return tree

# Function to navigate through the tree based on directions
def navigate_tree(tree, directions, current_node):
    #current_node = 'root'  # Starting from the root node
    num_steps = 0
    for direction in directions:
        if direction == 'L':
            next_node = tree[current_node][0]  # Move to the left node
            num_steps += 1
        elif direction == 'R':
            next_node = tree[current_node][1]  # Move to the right node
            num_steps += 1
        else:
            print("Invalid direction:", direction)
            return None  # Handle invalid direction

        if not next_node:  # If there's no connection in the given direction
            print("No node found in direction:", direction)
            return None
        current_node = next_node  # Update current node for the next iteration
    return [current_node, num_steps]  # Return the final node reached and number of steps taken


#-------------------------------------------------------
# # Part 1
# with open('input_day8.txt', 'r') as f:
#     lines = f.read() 
#     # Splitting the input into lines and filtering out empty lines
#     lines = [line.strip() for line in lines.split('\n') if line.strip()]

#     # Extracting directions and nodes
#     directions = lines[0]  # Assuming the first line represents directions
#     nodes = lines[1:]  # Assuming the rest are nodes

#     # Pass in all nodes to create the tree structure
#     tree = build_tree(nodes)
#     first_node = 'AAA'

#     #current_node = 'root'  # Starting from the root node
#     # Traverse the tree using given directions
#     result = navigate_tree(tree, directions, first_node)
#     final_node = result[0]
#     num_steps = result[1]
    
#     # for each character in directions
#     while (final_node != 'ZZZ'):
#             result = navigate_tree(tree, directions, final_node)
#             final_node = result[0]
#             num_steps += result[1]
#     print(num_steps)

#-------------------------------------------
# Part 2
with open('input_day8.txt', 'r') as f:
    lines = f.read() 
    # Splitting the input into lines and filtering out empty lines
    lines = [line.strip() for line in lines.split('\n') if line.strip()]

    # Extracting directions and nodes
    directions = lines[0]  # Assuming the first line represents directions
    nodes = lines[1:]  # Assuming the rest are nodes

    start_nodes = []

    for node in nodes:
        first_three = node[:3]  # Extract the first three letters
        if first_three[-1] == 'A':
            start_nodes.append(first_three)
    num_steps = [0]*len(start_nodes)

    # Pass in all nodes to create the tree structure
    tree = build_tree(nodes)

    # Traverse the tree using given directions
    # For each start node
    cycles = []
    for node in start_nodes:
        steps = 0
        for d in enumerate(cycle(directions), start=1):
            result = navigate_tree(tree, directions, node)
            node = result[0]
            steps += result[1]
            if node[2] == 'Z':
                cycles.append(steps)
                break

    # Calculate LCM of numbers in the list
    ans = math.lcm(*cycles)
    print(f"{ans=}")
