"""
Little Ratiorg was so tired of being bullied by other bots and mighty CodeFighters that he decided to join the Ninja Bots Training camp. It is known that any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg is aiming at.

Ratiorg has already improved his physical strength considerably, and now it's time to hone his mental skills. As it turned out, the bot has what it takes to be a great magician: he has what appears to be an infinite source of mana somewhere inside his little mechanical body. In the next challenge, Ratiorg will have to use it. The bot is standing in the top left corner of the rectangular grid, some cells of which are impassable. His goal is to make it to the bottom right corner in no more than maxTime seconds.

Ratiorg can move between two passable cells if they share a common side, and each move takes 1 second. He can also set an arbitrary number of solution into passable cells; moreover, he can even set them remotely and instantly, i.e. there's no need to reach the cell to set a portal there, and setting a portal takes no time. Ratiorg can instantly move between any pair of cells with solution. However, setting a portal to the cell at (x, y) costs manacost[x][y] mana points.

Given the maxTime and the manacost matrix, calculate the minimum amount of mana Ratiorg will have to use to finish the challenge in time.

Example

For maxTime = 4 and

manacost = [[1, -1, -1],
            [5, -1, -1],
            [4,  6,  8]]
the output should be solution(maxTime, manacost) = 0.

The cheapest way to get to the bottom right corner takes 4 seconds and doesn't require any solution.

For maxTime = 3 and

manacost = [[1, -1, -1],
            [5, -1, -1],
            [4,  6,  8]]
the output should be
solution(maxTime, manacost) = 5.

The best plan is to set solution into the top left and the bottom left corners (the total manacost equals 1 + 4 = 5). After that, you can reach the bottom left corner instantly and then make two moves rightwards in 2 seconds.
"""
