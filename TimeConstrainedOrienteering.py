"""
Not long ago you saw an orienteering competition on TV and immediately wanted to try it yourself. You've joined an orienteering club and started preparing for the upcoming competitions. You liked participation so much that you decided to organize your very own competition, and an unusual one.

In this race the participants should find such a path from start to finish that they will spend no more than T minutes on each road. When a participant leaves a location, the time on their stopwatch is set to T, and the countdown begins. If they can't make it to the next location in T seconds, they lose the race.

You have already picked a location for the start, but not yet settled for the finish. To decide which location to choose, for each of the n locations you'd like to calculate the minimum value of T that makes it possible to complete the race from start to this location.

Given the start location, the number of locations n and the roads connecting them, return the number of different minimum possible value of T for every finish location.

Example

For n = 5, start = 3, and

roads = [[1, 2, 3],
         [2, 3, 1],
         [2, 4, 2],
         [3, 5, 4],
         [4, 5, 3]]
the output should be
solution(n, start, roads) = 4.

The minimum possible values of T for locations from 1 to n are 3, 1, 0, 2 and 3 respectively, 4 distinct values in total.
"""
from collections import deque
def solution(n, start, roads):
    graph = [[] for i in range(n+1)]
    for [a,b,c] in roads:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    frontier, traversed = deque([(start,0)]), {start:0}
    while len(frontier) > 0:
        (node, max_T) = frontier.popleft()
        for [next_node, T] in graph[node]:
            next_max_T = max(max_T, T)
            if next_node not in traversed or traversed[next_node] > next_max_T:
                traversed[next_node] = next_max_T
                frontier.append((next_node, next_max_T))
    return len(set(traversed.values()))