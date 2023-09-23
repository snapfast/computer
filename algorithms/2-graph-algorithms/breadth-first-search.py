from collections import deque

def breadth_first_search(graph, start_point):
    """
    Perform a breadth-first search on a graph.

    Parameters:
    graph (dict): The graph represented as an adjacency list.
    start_point (int): The node to start the search from.

    Returns:
    list: The nodes visited during the search.
    """
    # Initialize a list to keep track of visited nodes
    visited_nodes = []

    # Initialize a queue using deque
    q = deque()

    # Add the start node to the visited nodes list and the queue
    visited_nodes.append(start_point)
    q.extend(graph[start_point])

    # While there are nodes in the queue
    while q:
        # Remove the first node from the queue
        n = q.popleft()

        # For each neighbor of the current node
        for i in graph[n]:
            # If the neighbor hasn't been visited yet
            if i not in visited_nodes:
                # Add it to the visited nodes list and the queue
                visited_nodes.append(i)
                q.append(i)
    
    # Return the list of visited nodes
    return visited_nodes

# Define a graph as an adjacency list
g = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4]
}

# Perform a breadth-first search on the graph starting from node 3
print(breadth_first_search(g, 3))