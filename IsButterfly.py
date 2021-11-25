'''
You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.

Today you want to teach your program to recognize butterfly patterns, which means that you need to implement a function that, given the adjacency matrix representing the contour, will determine whether it's a butterfly or not.

The butterfly contour looks like this:

A butterfly

Given the object's contour as an undirected graph represented by adjacency matrix adj determine whether it's a butterfly or not.

Example

For

adj = [[false, true, true, false, false],
       [true, false, true, false, false],
       [true, true, false, true, true],
       [false, false, true, false, true],
       [false, false, true, true, false]]
the output should be
solution(adj) = true.
'''
def solution(adj):
    return sorted([x.count(True) if x[y]!=True else 0 for y,x in enumerate(adj)])==[2,2,2,2,4]