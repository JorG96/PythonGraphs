'''
You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.

Today you want to teach your program to recognize star patterns in the image of the night sky, which means that you need to implement a function that, given the adjacency matrix representing a number of contours in the sky, will find the number of stars in it.

The graph representing some contour is cosidered to be a star if it is a tree of size 2 or if it is a tree of size k > 2 with one internal node (which is a tree root at the same time) and k - 1 leaves.
Here is an example of some stars:

'''

def solution(adj):    
    return sum(isStar(adj, i) for i in range(len(adj)))


def isStar(adj, i):
    star = sum(adj[i]) != 0 \
        and not adj[i][i] \
        and all(sum(row) == 1 for row in adj if row[i])
    # 0.5 for stars of size 2 as they are counted twice
    return star * (0.5 if sum(adj[i]) == 1 else 1) 