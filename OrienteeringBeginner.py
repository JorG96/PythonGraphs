"""
Not long ago you saw an orienteering competition on TV and immediately wanted to try it yourself. You've joined an orienteering club and started preparing for the upcoming competitions.

To test your skills, the coach asked you to enter the beginners' competition. In this race your objective is to reach the finish from the start by the shortest path. You were given a map that shows n different locations (including start and finish) connected by roads of different lengths. You are only allowed to traverse roads in one direction (i.e. all roads are one-way), but since this is competition for beginners the organizers chose such an orientation of the roads that if you constantly move along roads, you'll eventually reach the finish and if you leave some location you will never return there.

Given the number of locations n and the roads between them, find the length of the shortest path between the start (location with number 0) and the finish (location with number n - 1).

Example

For n = 6 and

roads = [[[1, 3]],
         [[4, 1], [3, 2]],
         [[1, 0]],
         [[5, 3]],
         [[5, 5]],
         []]
the output should be
solution(n, roads) = 8.
"""