# dfs uses recursion (which is a form of Stack)

def depth_first_search(graph, start_point):
    '''
    graph: dict
    start_point: node to start from
    nodes: total number of nodes
    '''
    visited_nodes = []

    # recursion baby


g = {
    1: [2, 3],
    2: [1],
    3: [2, 4],
    4: [3, 4, 5],
    5: [4]
}
print(type(g))
depth_first_search(g, 3)


