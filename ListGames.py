# Create a function ListGames(r,c) that generates a file with all possible "games."   A "game" is a board completely filled with x's and o's as if the players atlernated moves but did not check if either player won the game.  The number of x's is either equal to the number o's or greater by 1 depending on whether there are an even or odd number of squares.   This functions will be useful for finding won and drawn games.   We can use the list for later attempts at machine learning.

# This will result (r x c)!/((r x c) / 2)!)^2 or (r x c)!/((r x c) // 2)!)(((r x c) // 2 +1)!) games if r x c is even or odd respectfully.

# This list will not list all of the games since the order of play makes a difference in a game.   Also a game ends when either player gets n in a row.

import numpy as np
from itertools import permutations
# def ListGames(r, c):
  
# Waht follows is a sketch of a program that will do the job.  At the end, gamelist is a list of all the matrices in the form described in the intial remarks.

r = 2 #The number of rows
c = 3 # THe number of columns

matrix = np.empty((r,c), dtype=int)


#for i in range(2^(2*2)):
     #print(f'{i:04b}')

iterable = ''
for i in range((r * c) // 2): # Assuming r * c is even.  Need to write an if statement to handle r * c odd.
    iterable += '1'
    iterable += '0'

games = set(permutations(iterable, len(iterable)))

pairs = []
for i in range(r):
    for j in range(c):
        pairs.append((i, j))


sq = dict(zip(range(1, (r * c) + 1), pairs))
print(sq)

def move(rc, c):
    row = rc[0]
    col = rc[1]
    matrix[row, col] = c

gamelist=[]
for g in games:
    for i in range(1, (r * c) + 1):
        move(sq[i], int(g[i-1]))
    gamelist.append(matrix)

print(gamelist, len(gamelist))
