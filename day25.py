import networkx as nx
import matplotlib.pyplot as plt

# Function to find the three critical edges- we know for a fact that this graph can be separated into 2
# by cutting 3 edges
# We will still have to use for loops but instead of going through all of the edges, sorting them will increase the 
# likelyhood we find the 3 critical edges quicker so shouldnt have to go through them all
# Using sorted edges, loop over in sets of 3 to find the three edges to remove to split the graph into exactly 2
def find_critical_edges(graph):
    for i in range(len(sorted_edges) - 2):
        for j in range(i + 1, len(sorted_edges) - 1):
            for k in range(j + 1, len(sorted_edges)):
                edges_to_remove = [sorted_edges[i][0], sorted_edges[j][0], sorted_edges[k][0]]
                temp_graph = graph.copy()
                temp_graph.remove_edges_from(edges_to_remove)
                if nx.number_connected_components(temp_graph) == 2:
                    return edges_to_remove
    return None

# Create an empty graph
G = nx.Graph()

# Read input data and add nodes and edges to graph
with open('input_day25_test.txt', 'r') as file:
    for line in file:
        node, edges = line.strip().split(':')
        edges = edges.strip().split(' ')
        for c in edges:
            G.add_edge(node, c)

# Calculate edge betweenness centrality
edge_betweenness = nx.edge_betweenness_centrality(G)

# Sort edges by their betweenness centrality in descending order
sorted_edges = sorted(edge_betweenness.items(), key=lambda x: x[1], reverse=True)

# Find three critical edges to disconnect the graph into two components
critical_edges = find_critical_edges(G)
total = 1

if critical_edges:
    print("Critical edges to remove:")
    for edge in critical_edges:
        print(edge)

    # Remove the identified critical edges
    G.remove_edges_from(critical_edges)

    # Compute the number of nodes in the two resulting cluster
    new_communities = list(nx.connected_components(G))
    print("\nNumber of nodes in each resulting cluster after splitting:")
    # Multiply the number of nodes in two resulting clusters
    for i, community in enumerate(new_communities):
        print(f"Cluster {i+1}: {len(community)} nodes")
        total *= len(community)
    
    # Visualization of the modified graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_weight='bold')
    plt.title('Modified Graph')
    plt.show()

    # Print out answer
    print("Ans: ", total)
    
else:
    print("No combination of three critical edges found to disconnect the graph into two components.")
