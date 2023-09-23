
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
# dfs with stack only is available in separate file.

def depth_first_search(graph, start_point):
    '''
    graph: dict
    start_point: node to start from
    nodes: total number of nodes
    '''
    visited_nodes = []
    stack = []

    stack.append(start_point)

    while stack:
        # pop from the stack
        top_of_stack_element = stack.pop(-1)

        if top_of_stack_element not in visited_nodes:
            print(top_of_stack_element)
            visited_nodes.append(top_of_stack_element)

        for n in g[top_of_stack_element]:
            if n not in visited_nodes:
                stack.append(n)


g = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4]
}
print(type(g))
depth_first_search(g, 3)
