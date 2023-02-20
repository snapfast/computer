
'''

graph:

1: {2,3}
2: {1}
3: {1, 4}
4: {3}

if 1 is entrypoint, output will be: 1, 2, 3, 4
if 4 is entrypoint, output will be 4, 3, 1, 2


'''

# this dfs algorithm is for connected components only
# dfs uses recursion (which is a form of Stack)
# dfs with stack only is available in separate file.


def depth_first_search(graph, start_point):
    '''
    graph: dict
    start_point: node to start from
    nodes: total number of nodes
    '''
    visited_nodes = []
    q = []




g = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4]
}
print(type(g))
depth_first_search(g, 3)
