"""
You're working in a company that is specializing in optimizing various stuff. There are n rooms in your office connected by n corridors of different lengths. Your boss has told you that the company is going to repair all the corridors in the office one by one, and now you should choose one of the corridors that will be closed for repairs first.

Of course you, being a loyal employee of such a company, are quite fond of optimizations. That is why you want to close one of the corridors so that all the rooms are still connected to each other, and the total length of all the remaining corridors is the minimum possible. You understand that there can be more than one possible option, so now you want to calculate the number of different corridors that can be closed according to the conditions above.

Example

For n = 6 and

corridors = [[0, 1, 2], [1, 2, 3], [0, 2, 2], 
             [1, 3, 1], [2, 4, 2], [0, 5, 3]]
the output should be
solution(n, corridors) = 2.



Corridors connecting rooms 0 and 1 or rooms 0 and 2 can be closed for repairing.
"""
