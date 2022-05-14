
'''

graph:

1: {2,3}
2: {1}
3: {1, 4}
4: {3}

if 1 is entrypoint, output will be: 1, 2, 3, 4
if 4 is entrypoint, output will be 4, 3, 1, 2


'''

# this bfs algorithm is for connected components only
# BFS uses a Queue


def breadth_first_search(graph, start_point):
	'''
	graph: dict
	start_point: nodes to start from
	nodes: total number of nodes
	'''
	visited_nodes = []
	q = []

	visited_nodes.append(start_point)
	print(visited_nodes, q)

	# add points to q
	q.extend(graph[start_point])
	visited_nodes.extend(graph[start_point])

	print(visited_nodes, q)
	current_point = start_point
	print(visited_nodes, q)
	while q:
		print(visited_nodes, q)
		n = q.pop(0)
		for i in graph[n]:
			if i not in visited_nodes:
				visited_nodes.append(i)
				q.append(i)
	print(visited_nodes)


g = {
	1: [2, 3],
	2: [1],
	3: [1, 4],
	4: [3]
}
print(type(g))
breadth_first_search(g, 4)

