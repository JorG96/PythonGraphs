"""
Not long ago you got lost in the nearby woods when walking with your friend. You managed to get out of it, but no thanks to you: your friend was the one who drew the map of the woods and managed to find a way home. That embarrassed you quite a lot, so you decided to go out there to the other woods, get lost there and make your way home without any help.

The first part of your plan went smoothly, and now you're completely lost in unknown woods. You're on your own but for the map wmap you drew, and now you simply need to make it home, preferably before it gets too dark. To make things more interesting, you decided to find something unusual about the map you drew. Since you like even numbers even more than getting lost in the woods, you want to check if the map contains cycles only of even length. You firmly believe that such woods are magical, so you'll have something to tell your friend when you make it out safely.

Given the number of meadows in the woods n and the map representing their connections wmap, check if this map contains only cycles of even length.

Example

For n = 5 and wmap = [[1, 2], [1, 3], [1, 4], [0, 2], [4, 0]], the output should be
solution(n, wmap) = true.
There is only one cycle: 1 - 4 - 0 - 2 and its length is 4, which is an even number.

For n = 5 and wmap = [[1, 2], [1, 3], [1, 4], [0, 2], [4, 0], [1, 0]], the output should be
solution(n, wmap) = false.

There is a cycle 1 - 4 - 0, which length is 3 - an odd number.

"""

from collections import defaultdict
from collections import deque

def solution(n, wmap):
    adj_list = defaultdict(set)
    for s, e in wmap:
        if s == e:
            return False
        adj_list[s].add(e)
        adj_list[e].add(s)
        
    colors = [0 for i in range(n)]
    
    for i in range(n):
        for j in adj_list[i]:
            if colors[j] == 0:
                colors[j] = colors[i] + 1
            elif colors[j] == colors[i]:
                return False
    
    return True