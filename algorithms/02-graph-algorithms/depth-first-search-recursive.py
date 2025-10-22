# dfs uses recursion (which is a form of Stack)


def depth_first_search_recursion(graph, start_point, visited_nodes):
    if start_point not in visited_nodes:
        visited_nodes.append(start_point)

        if start_point not in graph:
            return visited_nodes

        # recursion
        for neighbour in graph[start_point]:
            depth_first_search_recursion(graph, neighbour, visited_nodes)
    return visited_nodes


g = {
    1: [2, 3],
    2: [1],
    3: [2, 4],
    4: [3, 4, 5],
    5: [4]
}
visited_nodes = []
print(depth_first_search_recursion(g, 2, visited_nodes))
