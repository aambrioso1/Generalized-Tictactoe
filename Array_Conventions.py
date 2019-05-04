# We begin with the follow structure.
# The board is a numpy array of integers.
# An empty square is represent by a 0.
# The first player’s moves are  represented by 1.
# The second player's moves are represented by -1.
# We adopt the convention that the squares are respresented by a tuple of integers (row, col).
# Also useful is the convention that the squares are numbered from 1 to m x n starting at the
# upper left and move across a row then to the next row.

import numpy as np

# Initialize the board array with m rows and n columns.
m = 3
n = 3

matrix = np.zeros(shape=(m,n), dtype = int)

print(matrix)
pairs = []
for i in range(m):
    for j in range(n):
        pairs.append((i,j))
print(pairs)
print(dict(zip(range(1,10),pairs)))

# Need to generalize and automate the construction of this dictionary with zip().
dict = dict(zip(range(1,10),pairs))

def move(rc, n):
    row = rc[0]
    col = rc[1]
    matrix[row, col] = n

move((1,1), 1)
move((0,0), -1)
move(dict[2], 1)
move(dict[3], -1)
move(dict[9], 1)

print(matrix)
