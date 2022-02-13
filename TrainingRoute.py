"""
Not long ago you saw an orienteering competition on TV and immediately wanted to try it yourself. You've joined an orienteering club and started preparing for the upcoming competitions.

One of the most important components of an orienteering competition is running. In order to train this skill you decided to practice on your club's special training field that consists of n locations numbered from 0 to n - 1, with some of them connected by two-way roads of different lengths. There are n roads in total, and any location is reachable from another one by the roads (possibly more than one). Your coach has composed a training route for you that consists of several locations that you should visit in the exact given order. Note, that you may be required to visit some location several times on your training route.

Given the number of locations n, roads between them and the training route, find the minimum possible total length of this route.

Example

For n = 6,

roads = [[[1, 50], [3, 10], [5, 4]],
         [[0, 50], [2, 15], [3, 5]], 
         [[1, 15], [4, 55]], 
         [[0, 10], [1, 5]],
         [[2, 55]], 
         [[0, 4]]]
and route = [5, 1, 0, 2], the output should be
solution(n, roads, route) = 64.

The shortest path between locations numbered 5 and 1 is of length 19, between 1 and 0 it's 15, and between 0 and 2 it's 30. The shortest route length is thus 19 + 15 + 30 = 64.
"""

def solution(n, roads, route):
    from collections import deque
    from heapq import heappop, heappush
    
    G = { k: set() for k in range(n) }
    W = {}
    for i, ends in enumerate(roads):
        for j, w in ends:
            G[i].add(j)
            if (i, j) not in W or w < W[(i, j)]:
                W[(i,j)] = w
                W[(j,i)] = w
    
    link_cnt = 0
    for ends in G.values():
        link_cnt += len(ends)
    link_cnt = int(link_cnt / 2)
    
    cycle = []
    if link_cnt == n:
        Q = [(0, [0])]
        while Q and not cycle:
            d, path = heappop(Q)
            i = path[-1]
            for j in G[i]:
                if j in path:
                    if j == path[-2]:  continue
                    k = path.index(j)
                    cycle = path[k:] + [j]
                    break
                heappush(Q, (d+1, path + [j]))

    cycle_w = []
    cn = len(cycle)
    for k in range(cn-1):
        i = cycle[k]
        j = cycle[k + 1]
        cycle_w.append(W[(i,j)])
    cycle_l = sum(cycle_w)

    B = { k: {} for k in cycle } if cn > 0 else { 0: {} }
    cycle_v = set(cycle)
    
    for start, prev in B.items():
        Q = deque([start])
        visited = {start} | cycle_v
        while Q:
            i = Q.popleft()
            nexts = G[i] - visited
            for j in nexts:
                prev[j] = i
                Q.append(j)
            visited |= nexts
    
    def get_path(k, prev):
        path = [k]
        while True:
            try:
                k = prev[path[-1]]
                path.append(k)
            except:
                return path[::-1]
        
    def distance(a, b):
        connect = { a: [-1, [a]], b: [-1, [b]] }
        connect[a][0] = cycle.index(a) if a in cycle else -1
        connect[b][0] = cycle.index(b) if b in cycle else -1
        for i, (ci, path) in connect.items():
            if ci != -1: continue
            for j, prev in B.items():
                if i not in prev: continue
                connect[i][0] = cycle.index(j) if j in cycle else -1
                connect[i][1] = get_path(i, prev)

        last_common = 0
        cycle_traverse = 0
        Ca = connect[a]
        Cb = connect[b]
        if Ca[0] == Cb[0]:
            for i in range(min(len(Ca[1]), len(Cb[1]))):
                if Ca[1][i] != Cb[1][i]:  break
                last_common = i
        else:
            u, v = Ca[0], Cb[0]
            u, v = min(u, v), max(u, v)
            d = 0
            for k in range(u, v):
                i = cycle[k]
                j = cycle[k+1]
                d += W[(i,j)]
            cycle_traverse = min(d, sum(cycle_w) - d)

        branch_traverse = 0
        for C in [Ca, Cb]:
            if len(C) == 1: continue
            for k in range(last_common, len(C[1]) - 1):
                i = C[1][k]
                j = C[1][k+1]
                branch_traverse += W[(i,j)]
        return branch_traverse + cycle_traverse

    ret = 0
    for k in range(len(route) - 1):
        i = route[k]
        j = route[k+1]
        ret += distance(i, j)
    return ret