'''
ou decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.

Today you want to teach your program to recognize wheel patterns, which means that you need to implement a function that, given the adjacency matrix representing the contour, will determine whether it's a wheel or not.

The wheel contour can be thought of as a single center vertex and a regular polygon with n (n > 2) vertices which are all connected to the center. Here is an example:
Given the object's contour as an undirected graph represented by its adjacency matrix adj determine whether it's a wheel or not.

Example

For

adj = [[false, true, true, true, true],
       [true, false, true, false, true],
       [true, true, false, true, false],
       [true, false, true, false, true],
       [true, true, false, true, false]]
the output should be
solution(adj) = true.
'''

def solution(adj):
    n = len(adj)
    for i in range(n):
        if adj[i][i]:
            return False
    numConnections = [sum(row) for row in adj]
    if n - 1 not in numConnections:
        return False
    numConnections.remove(n - 1)
    return all([nc == 3 for nc in numConnections])
