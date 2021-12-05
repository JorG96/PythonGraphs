"""
You've been studying trees a lot lately, and became an expert in caterpillar trees. Now that you know everything about them, you're ready to climb one. However, in order to climb such tree you need a special ladder that you call a mobius ladder.

A mobius ladder is a slightly modified proper ladder. Firstly, let's define what proper ladder is: a proper ladder is a ladder that can be represented by a graph containing two chains of vertices with n vertices in each one, where the ith vertex of the first chain is connected to the ith vertex of the second chain. For example, a proper ladder with 8 vertices looks like this:



A mobius ladder is a proper ladder with two more connections: the first vertex of the first chain is connected to the last vertex of the second chain, and last vertex of the first chain is connected to the first vertex of the second chain. For example, here is a mobius ladder with 8 vertices:



You found a ladder that can be represented by n vertices in the attic. Now you need to check if it is a mobius ladder, to make sure it can be used to climb a caterpillar tree.

Example

For n = 6 and ladder = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]], the output should be
solution(n, ladder) = false.



For n = 8 and

ladder = [[0, 1], [0, 2], [0, 7], [1, 3], [1, 6], [2, 3],
          [2, 4], [3, 5], [4, 5], [4, 6], [5, 7], [6, 7]]
the output should be solution(n, ladder) = true.

This is the test from the description:



For n = 10 and

ladder = [[0, 1], [0, 3], [0, 7], [0, 9], [1, 2],
          [1, 4], [1, 8], [2, 3], [2, 5], [2, 9],
          [3, 4], [3, 6], [4, 5], [4, 7], [5, 6],
          [5, 8], [6, 7], [6, 9], [7, 8], [8, 9]]
the output should be solution(n, ladder) = false.
"""
from collections import deque


def bfs(graph, source, target):
    """ Returns distance from source to target.
    """
    dist = {source: 0}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                if v == target:
                    return dist[v]
                if dist[v] > 2:
                    return -1
                queue.append(v)


def are_dist_ok(graph, n):
    """ Checks that distance among all the neighbors of every vertex is 2.
    """
    for i in range(n):
        if len([True for j in graph[i] if i != j]) != 3 or \
                [bfs(graph, graph[i][x], graph[i][y])
                 for x in range(2) for y in range(x + 1, 3)] != [2, 2, 2]:
            return False
    return True


def solution(n, ladder):
    """ Returns True if graph is Mobius ladder, False otherwise.
    """
    graph = [[] for _ in range(n)]  # adjacency list
    for u, v in ladder:
        graph[u].append(v)
        graph[v].append(u)

    if n == 4:  # check if it's a complete graph
        return all([len([True for j in graph[i] if j != i]) == 3 for i in range(n)])
    return are_dist_ok(graph, n)