"""
Little Ratiorg was tired of being bullied by other bots and mighty CodeFighters, so he joined the Ninja Bots Training camp. Any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg wants.

It's been several weeks, and Ratiorg is getting strong enough that he's making some enemies. They're starting to feel threatened, which is why they solutiond his next challenge. Here's how they did it:

Ratiorg is about to be locked up in one of multiple rooms in a rectangular hangar. The rooms are securely locked: it is possible to leave a room only in one direction specific to this room. The problem is, the villains have messed the system up, so now there is no way to finish the challenge from certain rooms. The challenge will be over if Ratiorg successfully leaves the hangar (i.e. leaves the rectangle that represents it).

To figure out the odds of Ratiorg's success, you'd like to calculate the number of rooms, starting from which Ratiorg won't be able to finish the challenge. Implement a function that will return this number.

Example

For

hangar = [['U', 'L'],
          ['R', 'L']]
the output should be
solution(hangar) = 2.

Ratiorg won't be able to get out of the hangar if he starts from either of the bottom rooms.
"""

def solution(hangar):
    row = len(hangar)
    col = len(hangar[0])
    directions = {'U': (-1,0), 'L': (0,-1), 'R' : (0, 1), 'D': (1,0)}
    reachable = numpy.full((row,col), -1)
    def dfs(x,y):
        stack = [[x,y]]
        while stack:
            x, y = stack.pop()
            if not reachable[x,y]  : return 0
            if reachable[x,y] == 1 : return 1
            i,j = directions[hangar[x][y]]
            if not (0 <= x + i < row and 0 <= y + j < col):
                return 1 
            else:
                if (x + i, y + j) not in keep_track : 
                    if 0 <= x + i < row and 0 <= y + j < col:
                        stack.append((x + i, y + j))
                        keep_track.add((x + i, y + j))
                else:
                    return 0
        return 0
    s = 0 
    for i in range(row):
        for j in range(col):
            keep_track = {(i, j)}
            k = dfs(i,j)
            if not k : s += 1
            for x,y in keep_track:
                reachable[x,y] = k
    return s
                
    
