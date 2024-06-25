import networkx as nx
import matplotlib.pyplot as plt

# dijkstra's algorithm
def dijkstra(graph, start):
    # Initialize distances and previous nodes
    distances = {node: float('infinity') for node in graph}
    # define start node to zero
    distances[start] = 0
    # define previous node in the optimal path from the source
    previous_nodes = {node: None for node in graph}
    # to list all nodes in the graph
    nodes = list(graph.keys())

    # loop runs until there are no more nodes to process
    while nodes:
        # node with the smallest distance that hasn't been processes yet
        current_node = min(nodes, key=lambda node: distances[node])
        # to remove the current node from the list of unprocessed nodes
        nodes.remove(current_node)

        # to check if the smallest distance is infinity,
        # the remaining nodes are not connected to the start node
        if distances[current_node] == float('infinity'):
            break

        # calculates an alternative route distance for each neighbour of the current node
        for neighbor, weight in graph[current_node].items(): # calculate new distance to neighbour
            alternative_route = distances[current_node] + weight
            # to updates the distance and record current node as the previous node,
            # if alternative route is shorter than the known distance
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_nodes[neighbor] = current_node

    # returns the shortest distances and the paths
    return distances, previous_nodes

# creating the graph
def create_graph():
    # define a weighted graph
    graph = {
        0: {1: 10}, # node 0 is connected to node 1 with a weight of 10
        1: {0: 10, 2: 5, 3: 15}, # node 1 connections
        2: {1: 5, 3: 10, 4: 30}, # node 2 connections
        3: {1: 15, 2: 10, 4: 10, 5: 5}, # node 3 connections
        4: {2: 30, 3: 10, 5: 20}, # node 4 connections
        5: {3: 5, 4: 20} # node 5 connections
    }
    return graph

# drawing the graph
def draw_graph(graph, previous_nodes, start_node):
    G = nx.Graph() # to initialize a new graph
    for node, edges in graph.items(): # to add edges to the graph
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight) # to add an egdes between node and neighbour with weight

    # to compute the positions of the nodes using the spring layout algorithm
    pos = nx.spring_layout(G)

    # to gets all edges of the graph along with their data
    edges = G.edges(data=True)

    # to create a dictionary of edge labels based on the weights
    edge_labels = {(u, v): d['weight'] for u, v, d in edges}

    # to draw the graph with node labels and edge labels to show the weights
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Highlight the shortest path
    for node in previous_nodes:
        # if the node is part of the path, get the path edges and draw path edges in red
        if previous_nodes[node] is not None:
            path_edges = [(previous_nodes[node], node)]
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

    # display the graph
    plt.show()

# main execution block
if __name__ == '__main__':
    graph = create_graph() # create the graph
    start_node = 0 # define the start node
    distances, previous_nodes = dijkstra(graph, start_node) # run dijkstra's algorithm

    print(f"Distances from node {start_node}:") # print distances from the start node
    for node, distance in distances.items(): # iterate through each node and distance
        print(f"Distance from node {start_node} to node {node} is {distance}") # print the distance

    draw_graph(graph, previous_nodes, start_node) # draw the graph with the shortest paths highlighted
