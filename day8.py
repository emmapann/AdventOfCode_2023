# Advent of code 2023
# day 8

# Build dict representing a tree-like structure
def build_tree(nodes):
    tree = {}
    first = True
    for node in nodes:
        # node structure is root = (left, right)
        root, rest = node.split('=')
        root = root.replace(' ','')
        if first:
            first_node = root
            first = False
            print("first node: ", first_node)

        rest = rest.replace('(', '').replace(')', '')
        left, right = rest.strip().split(',')
        tree[root] = (left.strip(), right.strip())  # Store left and right connections for each node
    last_node = root
    print("last node: ", last_node)
    return [tree, first_node, last_node]

# Function to navigate through the tree based on directions
def navigate_tree(tree, directions, current_node):
    #current_node = 'root'  # Starting from the root node
    num_steps = 0
    for direction in directions:
        # Infinite loop waiting for user input
        while True:
            user_input = input("Please enter something: ")
    
            # Check if user_input is not empty
            if user_input:
                break  # Exit the loop if user enters something

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
        print("direction: ", direction)
        print("next node: ", next_node)
        current_node = next_node  # Update current node for the next iteration

    return [current_node, num_steps]  # Return the final node reached and number of steps taken

with open('input_day8_test.txt', 'r') as f:
    lines = f.read() 
    # Splitting the input into lines and filtering out empty lines
    lines = [line.strip() for line in lines.split('\n') if line.strip()]

    # Extracting directions and nodes
    directions = lines[0]  # Assuming the first line represents directions
    nodes = lines[1:]  # Assuming the rest are nodes

    # Pass in all nodes to create the tree structure
    tree, first_node, last_node = build_tree(nodes)

    #current_node = 'root'  # Starting from the root node
    # Traverse the tree using given directions
    print("about to nav tree")
    result = navigate_tree(tree, directions, first_node)
    print("done")
    final_node = result[0]
    print("final_node: ", final_node)
    num_steps = result[1]
    
    # for each character in directions
    while (final_node != last_node):
            print("uh oh again")
            result = navigate_tree(tree, directions, final_node)
            final_node = result[0]
            print("final_node: ", final_node)
            num_steps += result[1]
    print(num_steps)