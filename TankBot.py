"""
Little Ratiorg was so tired of being bullied by other bots and mighty CodeFighters that he decided to join the Ninja Bots Training camp. It is known that any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg is aiming at.

His training is now officially over, and Ratiorg is ready to get back to CodeSignal and show who's the boss. To make his appearance more imposing, Ratiorg is planning to take a tank and drive it back home. However, the bot will have to travel through the forest covered in trees so strong that they can hold back even a tank, so not every tank can make it through this forest.

Since Ratiorg finished the trainings as the best student, he can pick any tank he likes. There are a lot of tanks of all possible sizes. All available tanks are square, can only move in one of the four directions (leftwards, rightwards, downwards or upwards), and can't move over the trees.

The Ninja Bots Training camp is located at the top left corner of the forest, and CodeFigts bots camp is located at its bottom right corner. Given the map of the forest, find the maximum size of the tank Ratiorg can take in order to get from the training camp to the CodeFigths bot camp.

Example

For

forest =  [[true, true, true,  true],
           [true, true, false, true],
           [true, true, true,  true],
           [true, true, true,  true]]
the output should be
solution(forest) = 2.



For

forest = [[false, true, true],
          [true,  true, true]]
the output should be
solution(forest) = 0.

There is a tree right at the entrance of the Training Camp, so there's no way to get out of there by tank.


"""
import numpy as np


def solution(forest):

    if 0 in (forest[0][0], forest[-1][-1]):
        return 0
    forest = np.array(forest)
    L, W = len(forest), len(forest[0])
    m = min(L, W)
    i, j = 1, 2
    while i < m:  # find max size of tank in top left corner
        if False in forest[i, :i + 1] or False in forest[:i, i]:
            break
        i += 1
    while j < m:  # find max size of tank in bottom right corner
        if False in forest[-j, -j:] or False in forest[-j:, -j]:
            break
        j += 1
    size = min(i, (j - 1, j)[j == m])  # choose smaller size between above mentioned, or smaller dimension
    while size:
        visited = set()
        pool = [((0, 0), (size - 1, size - 1))]
        while pool:
            (r1, c1), (r2, c2) = pool.pop()  # tank
            if (r2, c2) == (L - 1, W - 1):  # bottom right corner of tank == bottom right corner of forest
                return size
            abs_i = r2 * W + c2
            visited.add(abs_i)
            if c1 and abs_i - 1 not in visited and False not in forest[r1: r2 + 1, c1 - 1]:  # move left
                pool.append(((r1, c1 - 1), (r2, c2 - 1)))
            if r1 and abs_i - W not in visited and False not in forest[r1 - 1, c1: c2 + 1]:  # move top
                pool.append(((r1 - 1, c1), (r2 - 1, c2)))
            if c2 < W - 1 and abs_i + 1 not in visited and False not in forest[r1:r2 + 1, c2 + 1]:  # move right
                pool.append(((r1, c1 + 1), (r2, c2 + 1)))
            if r2 < L - 1 and abs_i + W not in visited and False not in forest[r2 + 1, c1: c2 + 1]:  # move bottom
                pool.append(((r1 + 1, c1), (r2 + 1, c2)))
        size -= 1
    return 0
            
        
        