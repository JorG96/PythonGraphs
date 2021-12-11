"""Little Ratiorg was tired of being bullied by other bots and mighty CodeFighters, so he joined the Ninja Bots Training camp. Any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg wants.

Ratiorg aced the very first challenge, and is ready to begin the second. The little bot is given a canvas, each pixel of which has some color. Ratiorg should apply several flood fill operations to the canvas, and show the resulting image to the judges. Each flood fill operation is given as an array of three elements [x, y, color], where (x, y) is the coordinates of the pixel to which the operation is applied, and color is the color with which the pixel and its area should be painted. The area that should be painted along with the initial pixel is defined as follows:

Initially, only the pixel to which the operation was applied should be painted.
Consider all pixels that are adjacent to the initial one (i.e. directly above, below, to the left or to the right of it). If the difference between the color of this pixel and the color of the initial one is not greater than d, this pixel should also be painted.
For each pixel painted on this step consider all its neighbors in the same manner.
Your task is to help the judges check Ratiorg's performance. Given canvas, operations and the value of d, return the state of the image after all operations have been applied.

Example

For

canvas = [[0, 1, 5, 2, 4, 2, 6],
          [5, 2, 4, 6, 2, 0, 0],
          [3, 3, 3, 7, 8, 3, 2],
          [2, 1, 1, 0, 0, 0, 0]]
operations = [[0, 0, 10], [1, 3, 3]], and d = 3,
the output should be

solution(canvas, operations, d) = [[10, 10,  3,  2,  4, 10, 6 ],
                                     [ 5, 10,  3,  3, 10, 10, 10],
                                     [10, 10, 10,  3,  3, 10, 10],
                                     [10, 10, 10, 10, 10, 10, 10]]
"""
def solution(canvas, operations, d):
    h, w = len(canvas), len(canvas[0])
    
    def fill(node, init, color):
        matches = set()
        q = [node]
        while q:
            i, j = q.pop()
            if not (0 <= i < h and 0 <= j < w):
                continue
            elif (i,j) in matches:
                continue
            if abs(canvas[i][j] - init) <= d:
                matches.add((i, j))
                q.append((i+1, j))
                q.append((i-1, j))
                q.append((i, j+1))
                q.append((i, j-1))
        for i,j in matches:
            canvas[i][j] = color
    
    for i, j, color in operations:
        fill((i, j), canvas[i][j], color)
    return canvas