"""
You've just become a director of a big company. As it turned out, the company favors one-on-one meetings, which is why there are so many of them each week. Each meeting has an integer efficiency value that shows how much profit it gives the company. In order to make your employees chat less and work more, you'd like remove some one-on-one's from the weekly schedule and leave as few meetings as possible. Of course, there are some restrictions:

it should still be possible to deliver information from any employee to any other one (probably, it'll take a bunch of meetings to deliver a piece of information from one worker to the other one);
there should be as few meetings left as possible;
the total efficiency should be the maximum possible. The total efficiency equals the sum of efficiencies of all one-on-one's left.
Given the number of people in the company n and the list of current one-on-one meetings with their efficiency values, find the best total efficiency of the reduced scheme.

Example

For n = 4 and meetings = [[0, 1, 3], [1, 2, 2], [3, 0, 1], [3, 2, 5]],
the output should be
solution(n, meetings) = 10.

The best way to reduce meetings is to remove the 3rd (1-based) meeting from the list.
"""
def solution(n, meetings):
    from heapq import heappop as pop, heappush as push 
    from collections import defaultdict as ddict
    g = ddict(dict)
    for x,y,z in meetings:
        g[x][y] = g[y][x] = z 
    visited = [0] * n 
    queue = [(0,0)]
    total = 0
    while queue:
        weight, node = pop(queue)
        if not visited[node]:
            visited[node] = 1 
            total -= weight 
            for v,w in g[node].items():
                if not visited[v]:
                    push(queue,(-w,v))
    return total