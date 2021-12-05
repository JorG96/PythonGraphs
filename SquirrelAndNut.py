"""
Wandering in the woods, you noticed a squirrel sitting in node A of a tree. It didn't look like it was going to sit there forever though: there was a delicious nut in node B, and the squirrel looked determined to reach it by moving via the branches of the tree. You grabbed your camera to take a picture of the squirrel in node C (that's the only node that would make the picture perfect), but was too late: the smart rodent had already made it to node B.

There are still a lot of nuts on the tree, and it seems that the squirrel is going to try and take them all. Looks like the squirrel is smart enough to follow only the shortest paths along the tree branches, which means you can now predict when the right opportunity to take a perfect picture arises. Given configuration of the tree and a bunch of triples consisting of numbers A, B and C, for each triple return true if the squirrel will run through node C on its path from A to B, and false otherwise.

It is guaranteed that each node has no more than 5 branches.

Example

For

tree = [1, 2,
        1, 3,
        2, 4,
        3, 5,
        3, 6]
and

triples = [[4, 6, 3],
           [1, 4, 2],
           [5, 6, 1]]
the output should be
solution(tree, triples) = [true, true, false].
"""
