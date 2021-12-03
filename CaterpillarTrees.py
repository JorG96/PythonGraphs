"""
Not long ago you discovered a wonderful tree in the nearby woods that made you very curious about the greenery around you. You went to the nearby woods and drew various plants in your notebook. The plants in the woods have various structures: some of them even contain loops!

Anyway, for now you are interested only in trees. You came up with a brand new property: you call a tree a caterpillar if there exists a path in it, such that each vertex of a tree either belongs to this path or is connected to one of its vertices by a single edge. To find out more about them, you would like to write a program that will find all interesting trees in the structures you drew in your notebook.

The plants you drew consist of n vertices and are connected by several edges. Calculate the number of regular trees and caterpillar trees in the structures you drew in your notebook.

Example

For n = 21 and

edges = [[0, 1], [1, 2], [2, 3], [2, 4], [4, 5], [4, 6], [4, 7],
         [4, 8], [4, 9], [4, 10], [10, 11], [11, 12], [11, 13],
         [11, 14], [14, 15], [14, 16], [14, 17], [14, 18], [14, 19]]
the output should be solution(n, edges) = [2, 2].
There are two connected components and both of them are trees and caterpillar trees.

For n = 22 and

edges = [[0, 1], [1, 2], [2, 3], [2, 4], [4, 5], [4, 6], [4, 7],
         [4, 8], [4, 9], [4, 10], [10, 11], [11, 12], [11, 13],
         [11, 14], [14, 15], [14, 16], [14, 17], [14, 18], [14, 19], [13, 20]]
the output should be solution(n, edges) = [2, 1].

The first connected component is a tree, but not a caterpillar tree, because vertex 20 is not directly connected to the central path.
"""
def solution(n, edges):
    import sys
    sys.setrecursionlimit(200000)
    visited = [False] * n
    component = [-1] * n
    color = [0] * n
    deg = [0] * n
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1
    initial_deg = deg[:]
    count = 0
    vertices = []
    for u in range(n):
        if not visited[u]:
            vertices.append(dfs(u, adj, color, visited, component, count, 1))
            count += 1
    edges_count = [0] * count
    for u, v in edges:
        assert(component[u] == component[v])
        edges_count[component[u]] += 1
    trees = 0
    caterpillars = 0
    components = len(vertices)
    for i in range(components):
        if edges_count[i] == len(vertices[i]) - 1:
            trees += 1
        non_leafs = []
        for u in vertices[i]:
            if initial_deg[u] == 1:  # leaf
                for v in adj[u]:
                    deg[v] -= 1
            else:  # non-leaf
                non_leafs.append(u)
        non_leaf_degs = sorted(map(lambda x: deg[x], non_leafs))
        assert len(non_leaf_degs) == 0 or min(non_leaf_degs) >= 0
        if len(non_leaf_degs) == 0 or max(non_leaf_degs) <= 2:
            if len(non_leaf_degs) == 0:
                caterpillars += 1
            elif len(non_leaf_degs) == 1:
                if non_leaf_degs[0] == 0:
                    caterpillars += 1
            elif len(non_leaf_degs) == 2:
                if non_leaf_degs[0] == non_leaf_degs[1] == 1:
                    caterpillars += 1
            else:
                if non_leaf_degs[0] == non_leaf_degs[1] == 1 and non_leaf_degs[2] == 2:
                    caterpillars += 1
    return [trees, caterpillars]
            
def dfs(u, adj, color, visited, component, count, cur_color):
    vertices = [u, ]
    visited[u] = True
    color[u] = cur_color
    component[u] = count
    for v in adj[u]:
        if not visited[v]:
            vertices.extend(dfs(v, adj, color, visited, component, count, 3 - cur_color))
    return vertices