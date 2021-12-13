"""
Little Ratiorg was tired of being bullied by other bots and mighty CodeFighters, so he joined the Ninja Bots Training camp. Any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg wants.

It's been several weeks, and Ratiorg already feels how much stronger he has become. However, Ratiorg is about to face his first really exciting challenge: the Electric Field. It works like this: the bot stays in the top left corner of a rectangular grid. In one move he can walk to one of the nearest cells (directly above, below, to the left or to the right of his current position). Ratiorg's goal is to get to the bottom right corner in the least possible number of moves. However, it's not as simple as it seems: there are electric wires running through the grid. If Ratiorg steps on a wire, his microchips will be burnt to a crisp, so Ratiorg, prudent bot that he is, wants to do his best to avoid them.

You want to give Ratiorg a hint by telling him the least possible number of moves required to get to the destination. Given the grid and the wires, return the minimum number of moves required to get to the bottom right corner from the top left corner. If it's not possible to get there, return -1 instead.

Example

For grid = [4, 8] and

wires = [[1, 0, 1, 3], [3, 1, 3, 2], [4, 1, 4, 3], [4, 2, 4, 4],
         [1, 3, 3, 3], [2, 1, 7, 1], [2, 2, 7, 2], [5, 3, 8, 3]]
the output should be
solution(grid, wires) = 26.
"""
def solution(grid, wires):

    G = dict()
    for i in range(grid[1]):
        for j in range(grid[0]):
            G[(i,j)] = []
            for x,y in [(i+1,j), (i-1,j), (i,j+1), (i, j-1)]:
                if x >=0 and y>=0 and x < grid[1] and y < grid[0]:
                    G[(i,j)].append((x,y))
    for w in wires:
        if w[0] == w[2]:
            x = w[0]
            lo, hi = min(w[1], w[3]), max(w[1], w[3])
            for y in range(lo, hi):
                a = (x,y)
                b = (x-1, y)
                if b in G.get(a,[]):
                    G[a].remove(b)
                if a in G.get(b,[]):
                    G[b].remove(a)
            
        elif w[1] == w[3]:
            y = w[1]
            lo, hi = min(w[0], w[2]), max(w[0], w[2])
            for x in range(lo, hi):
                a = (x,y)
                b = (x, y-1)
                if b in G.get(a,[]):
                    G[a].remove(b)
                if a in G.get(b,[]):
                    G[b].remove(a)
    goal = (grid[1]-1, grid[0]-1)                
    return dfs(G, goal)
def dfs(G, end):
    queue = [(0,0)]
    
    prev = {(0,0): None}
    
    while queue:
        cur = queue.pop(0)
        for n in G[cur]:
            if n not in prev:
                queue.append(n)
                prev[n] = cur
    if end not in prev:
        return -1
    path = []
    cur = end
    while cur:
        path.append(cur)
        cur = prev[cur]
    print(path[::-1])
    return len(path) -1