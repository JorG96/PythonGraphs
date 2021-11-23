'''
Once upon a time, in a kingdom far, far away, there lived a King Byteasar III. As a smart and educated ruler, he did everything in his (unlimited) power to make every single system within his kingdom efficient. The king went down in history as a great road builder: during his reign a great number of roads were built, and the road system he created was the most efficient during those dark times.

When you started learning about Byteasar's III deeds in your history classes, a creeping doubt crawled into the back of your mind: what if the famous king wasn't so great after all? According to the most recent studies, there were n cities in Byteasar's kingdom, connected by two-way roads. You managed to get information about these roads from the university library, so now you can write a function that will determine whether the road system in Byteasar's kingdom was efficient or not.

A road system is considered efficient if it is possible to travel from any city to any other city by traversing at most 2 roads.

Example

For n = 6 and

roads = [[3, 0], [0, 4], [5, 0], [2, 1],
          [1, 4], [2, 3], [5, 2]]
the output should be
solution(n, roads) = true.

For n = 6 and

roads = [[0, 4], [5, 0], [2, 1],
          [1, 4], [2, 3], [5, 2]]
the output should be
solution(n, roads) = false.

As you can see, it's only possible to travel from city 3 to city 4 by traversing at least 3 roads.
'''
from collections import defaultdict

def solution(n, roads):
    vertices = defaultdict(set)
    
    for road in roads:
        x, y = road
        vertices[x].add(y)
        vertices[y].add(x)
    
    for i in range(n):
        for j in range(i + 1, n):
            if i in vertices[j] or j in vertices[i] or len(vertices[i] & vertices[j]) >= 1:
                continue
            else:
                return False
    print(vertices)
    return True

