"""
Little Ratiorg was so tired of being bullied by other bots and mighty CodeFighters that he decided to join the Ninja Bots Training camp. It is known that any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg is aiming at.

Ratiorg has become so cool that the authorities decided to send him on a special mission to the remote cuboid planet of size a × b × c, not yet inhabited by bots. In order to prepare for the mission, Ratiorg has to understand the properties of the planet by training on its net here, on Earth. Here's how the planet and the net on which the bot is going to prepare for the mission look like:

 

The net is divided into 6 areas, with each area representing one of the planet's surfaces. Each of the areas is divided into a grid with cells of size 1 × 1, with some of the cells being impassable. The coordinates of each cell can be represented in the format (area, row, column), where area stands for the area number shown in the net image above, and (row, column) stands for 0-based cell's position in this area. It is possible to move between two cells if they share a common side.

Ratiorg would like understand how close the net he's going to train on is to the conditions of the planet. In order to do this, he would like to calculate the difference between the numbers of pairs of cells that are reachable from one another on a cuboid and the number of pairs of cells that are reachable from one another on a net (note that only pairs of different cells should be counted, and the order of cells in a pair doesn't matter, i.e. (a, b) is the same pair as (b, a)).

Given the dimensions of the cuboid and the impassableCells, calculate the value Ratiorg is interested in.

Example

For cuboid = [1, 2, 3] and
impassableCells = [[1, 0, 0], [3, 0, 1], [3, 2, 0], [4, 0, 1], [5, 1, 0]],
the output should be
solution(cuboid, impassableCells) = 106.

On a cuboid, all cells but the impassable ones are reachable from one another, so the total number of reachable pairs equals 17 * 16 / 2 = 136.

Here's how the net of this cuboid looks like:



There are four areas in which all cells are connected. Thus, the number of pairs of cells that are reachable from one another is
3 * 2 / 2 + 4 * 3 / 2 + 4 * 3 / 2 + 6 * 5 / 2 = 30.

Thus, the answer is 136 - 30 = 106.
"""
def solution(cuboid, impassableCells):
    
    import sys
    sys.setrecursionlimit(10**6)
    #Step 1, create separate area arrays and add obstructions
    import numpy as np
    a, b, c = cuboid
    zero, one, two, three, four, five = np.ones((a, c)), np.ones((a, b)), np.ones((a, c)), np.ones((c, b)), np.ones((a, b)), np.ones((c, b))
    
    d = {0:zero, 1:one,  2:two, 3:three, 4:four,  5:five}
    for area, x, y in impassableCells:
        d[area][x, y] = 0
        
    
    #2.  Create 6 different adjacency matrices
    def adjacent(x, y, area, areaCode):
        nr, nc = area.shape
        all_moves = [(x - 1, y),(x + 1, y), (x, y + 1), (x, y - 1)]
        return [(areaCode, a, b) for a, b in all_moves if 0 <= a < nr and 0 <= b < nc and area[a, b]]
    
    adj_lists = []
    for a in d:
        area = d[a]        
        nr, nc = area.shape
        adj_lists.append({(a, i, j): adjacent(i, j, area, a)for i in range(nr) for j in range(nc) if area[i, j]})
        
    
    #3. Find connected components of these individual areas
    
    def dfs(s, adjList, cc):
        if s not in cc:
            cc.add(s)
            for adj in adjList[s]:
                dfs(adj, adjList, cc)    
    
    connectedComponents = {}
    

    #Merge adj_lists to create new one for the net
    netAdjList = {cell:list(areaAdjList[cell]) for areaAdjList in adj_lists for cell in areaAdjList}
    a, b, c = cuboid
    
    #Create links between areas 0, 1, and 2:
    for r in range(a):
        lkey, rkey = (0, r, c - 1), (1, r, 0)
        if lkey in netAdjList and rkey in netAdjList:
            netAdjList[lkey].append(rkey)
            netAdjList[rkey].append(lkey)
        
        lkey, rkey = (1, r, b - 1), (2, r, 0)
        if lkey in netAdjList and rkey in netAdjList:
            netAdjList[lkey].append(rkey)
            netAdjList[rkey].append(lkey)
    
    #Create link between 1 and 3, 3 and 4 and 4, 5    
    
    
    for col in range(b):        
        ukey, bkey = (1, a - 1, col), (3, 0, col)
        if ukey in netAdjList and bkey in netAdjList:
            netAdjList[ukey].append(bkey)
            netAdjList[bkey].append(ukey)
            
        ukey, bkey = (3, c - 1, col), (4, 0, col)
        if ukey in netAdjList and bkey in netAdjList:
            netAdjList[ukey].append(bkey)
            netAdjList[bkey].append(ukey)        
    
        ukey, bkey = (4, a - 1, col), (5, 0, col)        
        if ukey in netAdjList and bkey in netAdjList:
            netAdjList[ukey].append(bkey)
            netAdjList[bkey].append(ukey)                
    
    
    visited = set()
    cc_lengths = []
    for k in netAdjList:
        if k not in visited:
            cc = set()
            dfs(k, netAdjList, cc)
            cc_lengths.append(len(cc))            
            visited.update(cc)

    net_combinations = sum(map(lambda x: x * (x - 1) //2, cc_lengths))
    
    #Continue updating  the netAdjList to form the adj list for cube 
    #Join bottom of 0 to left of 3 (reversed) and bottom of 2 to right of 3(reversed),
    ## top of 0 to left of 5 and top of 2 to right of 5
    for col in range(c):
        lkey, rkey = (0, a - 1, col), (3, c - col - 1, 0)
        if lkey in netAdjList and rkey in netAdjList:
            netAdjList[lkey].append(rkey)
            netAdjList[rkey].append(lkey)
        
        lkey, rkey = (3, col, b - 1), (2, a - 1, col)
        if lkey in netAdjList and rkey in netAdjList:
            netAdjList[lkey].append(rkey)
            netAdjList[rkey].append(lkey)     
        
        lkey, rkey = (0, 0, col), (5, col, 0)
        if lkey in netAdjList and rkey in netAdjList:
            netAdjList[lkey].append(rkey)
            netAdjList[rkey].append(lkey)
            
        lkey, rkey = (5, c - col - 1, b - 1), (2, 0, col)
        if lkey in netAdjList and rkey in netAdjList:
            netAdjList[lkey].append(rkey)
            netAdjList[rkey].append(lkey)            
            
                
    #connect left of 0 to left of 4 and right of 2 to right of 
    for row in range(a):
        lkey, rkey = (0, row, 0), (4, a - row - 1, 0)
        if lkey in netAdjList and rkey in netAdjList:
            netAdjList[lkey].append(rkey)
            netAdjList[rkey].append(lkey)
            
        lkey, rkey = (4, a - row - 1, b - 1), (2, row, c - 1)
        if lkey in netAdjList and rkey in netAdjList:
            netAdjList[lkey].append(rkey)
            netAdjList[rkey].append(lkey)        
        
    #Connect top of 1 to bottom of 5
    for col in range(b):
        lkey, rkey = (1, 0, col), (5, c - 1, col)        
        if lkey in netAdjList and rkey in netAdjList:
            netAdjList[lkey].append(rkey)
            netAdjList[rkey].append(lkey)        
    
    #Find connected components again
    visited = set()
    cc_lengths = []
    ccs = []
    for k in netAdjList:
        if k not in visited:
            cc = set()
            dfs(k, netAdjList, cc)
            cc_lengths.append(len(cc))
            if len(cc) == 1:
                ccs.append(cc)
            visited.update(cc)         
            
    cube_combinations = sum(map(lambda x: x * (x - 1) //2, cc_lengths))

    return cube_combinations - net_combinations