"""
Not long ago you saw an orienteering competition on TV and immediately wanted to try it yourself. You've joined an orienteering club and started preparing for the upcoming competitions. You liked participation so much decided to organize your very own competition, and an unusual one.

In this race the participants should find such a path from start to finish that they will spend no more than T minutes on each road. When a participant leaves a location, the time on their stopwatch is set to T, and the countdown begins. If they can't make it to the next location in T seconds, they lose the race.

You haven't yet chosen locations for the start and for the finish. To decide which locations to chose, for each ordered pair of locations (a, b) you'd like to calculate the minimum value of T that makes it possible to complete the race that starts at a and finishes at b.

Given the number of locations n and one-way roads connecting them, for every start and every finish locations return the minimum possible value of T.

Example

For n = 3 and

roads = [[0, 1, 100000],
         [5, 0, 2],
         [4, -1, 0]]
the output should be

solution(n, roads) = [[0, 1, 2],
                      [4, 0, 2],
                              
"""

def solution(n, m):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if 0 <= m[i][k] and 0 <= m[k][j]:
                    if 0 <= m[i][j]:
                        m[i][j] = min(m[i][j], max(m[i][k], m[k][j]))
                    else:
                        m[i][j] = max(m[i][j], m[i][k], m[k][j])
                    
    return m