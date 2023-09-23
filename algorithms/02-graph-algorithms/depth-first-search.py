from typing import Dict, List

def depth_first_search(graph: Dict[int, List[int]], start_point: int) -> None:
    """
    Perform a depth-first search on a graph.

    Parameters:
    graph (dict): The graph represented as an adjacency list.
    start_point (int): The node to start the search from.

    Returns:
    None
    """
    # Initialize a list to keep track of visited nodes
    visited_nodes = []

    # Initialize a stack and add the start node
    stack = [start_point]

    while stack:
        # Pop the top node from the stack
        current_node = stack.pop()

        # If the node hasn't been visited yet
        if current_node not in visited_nodes:
            print(current_node)
            visited_nodes.append(current_node)

        # Add the neighbors of the current node to the stack
        for neighbor in graph[current_node]:
            if neighbor not in visited_nodes:
                stack.append(neighbor)
    
    # return the nodes visited
    return visited_nodes

if __name__ == "__main__":
    # Define a graph as an adjacency list
    graph = {
        1: [2],
        2: [1, 3],
        3: [2, 4],
        4: [3, 5],
        5: [4]
    }

    # Perform a depth-first search on the graph starting from node 3
    visited_nodes = depth_first_search(graph, 3)
    print("Nodes visited during DFS:", visited_nodes)