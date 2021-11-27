"""
You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.

Today you want to teach your program to recognize flower patterns, which means that you need to implement a function that, given the adjacency matrix representing the contour, will determine whether it's a flower or not.

The flower contour consists of several (at least one) petals.
Petal contours are the same-sized (of size greater than 2) complete graphs with exactly one common vertex.
Given the object's contour as an undirected graph represented by adjacency matrix adj determine whether it's a flower or not.

Example

For

adj = [[false, true, true, true, true],
       [true, false, true, false, false],
       [true, true, false, false, false],
       [true, false, false, false, true],
       [true, false, false, true, false]]
the output should be
solution(adj) = true.
"""
def solution(adj):
    petalRank, solutionSignature = flowerSignature(adj)
    return solutionSignature and not isSelfConnecting(adj) and getNPetals(adj) * petalRank == len(adj) - 1
    

def isSelfConnecting(adj):
    return any(adj[i][i] for i in range(len(adj)))

def flowerSignature(adj):
    counts = sorted(sum(row) for row in adj)
    petalRank = counts[0]
    return petalRank,  petalRank >= 2 and counts[-1] == len(adj) - 1 and all(petalRank == c for c in counts[:-1])

def getNPetals(adj):
    removeCenter(adj)
    n = 0
    for i, row in enumerate(adj):
        if any(row):
            n += 1
            removeConnectedTrues(adj, i)
    return n
    
def removeCenter(adj):
    center = max(range(len(adj)), key=lambda i: sum(adj[i]))
    for i in range(len(adj)):
        adj[center][i] = adj[i][center] = False
    
def removeConnectedTrues(adj, j):
    for i in range(len(adj)):
        if adj[i][j]:
            adj[i][j] = adj[j][i] = False
            removeConnectedTrues(adj, i)
