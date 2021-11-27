'''
You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.

Today you want to teach your program to recognize tadpole patterns, which means that you need to implement a function that, given the adjacency matrix representing the contour, will determine whether it's a tadpole or not.

The tadpole contour consists of two parts: a head which is a cycle with n (n > 2) vertices, and a tail which is a simple path (with at least one vertex) connected to the head.
Given the object's contour as an undirected graph represented by its adjacency matrix adj determine whether it's a tadpole or not.

Example

For

adj = [[false, true, true, false, false],
       [true, false, false, true, false],
       [true, false, false, true, false],
       [false, true, true, false, true],
       [false, false, false, true, false]]
the output should be
solution(adj) = true.
'''
def solution(adj):
    # A graph is a tadpole iff the graph has the degree
    # sequence 1, 2, 2, ..., 2, 2, 3 and is connected.

    expectedDegseq = [2] * len(adj)
    expectedDegseq[0] = 1
    expectedDegseq[-1] = 3
    
    if sorted(sum(row) for row in adj) != expectedDegseq:
        return False
    
    # Check that the graph is connected.
    q = [0]
    seen = {0}
    while q:
        u = q.pop(0)
        for v in range(len(adj)):
            if adj[u][v] and v not in seen:
                q.append(v)
                seen.add(v)
    
    return len(seen) == len(adj)

