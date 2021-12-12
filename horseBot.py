"""
Little Ratiorg was tired of being bullied by other bots and mighty CodeFighters, so he joined the Ninja Bots Training camp. Any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg wants.

The little bot has already successfully completed several challenges. Now he is facing a challenge in which he has to prove that he knows how to ride a horse and plan battles. Ratiorg is sitting on his digital horse in the top left corner of an n × m board. The horse can only make moves similar to those of a knight chess piece. Prior to any action, Ratiorg should define values a and b (0 < a ≤ b), which will specify the horse's moves: each move the horse will change one of its coordinates by a, and the other one by b.

Ratiorg needs to define such a and b that will let him end up in the bottom right corner. How many ways are there to do this?

Example

For n = 3 and m = 3, the output should be
solution(n, m) = 3.

Ratiorg can define three pairs: (1, 1), (1, 2) and (2, 2)
"""
import numpy as np

def solution(n, m):
    if m < n:
        n, m = m, n

    finish = (n-1, m-1)

    def steps(i, j, a, b):
        options = [(i+a, j+b), (i+a, j-b),
                   (i-a, j+b), (i-a, j-b),
                   (i+b, j+a), (i+b, j-a),
                   (i-b, j+a), (i-b, j-a)]
        return ((x,y) for x,y in options
                if 0 <= x < n and 0 <= y < m)
    
    def walk(a, b):
        seen = set((0, 0))
        q = [(0, 0)]
        while q:
            pos = q.pop()
            for s in steps(*pos, a, b):
                if s == finish:
                    return True
                if s not in seen:
                    seen.add(s)
                    q.append(s)
        return False
    
    count = 0
    for a in range(1, n):
        for b in range(a, m):
            count += walk(a, b)
    return count