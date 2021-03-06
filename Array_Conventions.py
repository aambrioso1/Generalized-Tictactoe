import numpy as np
# We begin with the following structure.
# The board is a numpy array of integers.
# An empty square is empty.
# The first player’s moves are  represented by 1.
# The second player's moves are represented by 0.
# We adopt the convention that the squares are represented by a tuple of integers (row, col).
# We will also use the convention that the squares are numbered from 1 to (number of rows) x (number of columns) starting at the
# upper left and moving across a row then to the next row.


# Initialize the board array with m rows and n columns.
m = 3
n = 3

matrix = np.empty(shape=(m, n), dtype=int)

print(matrix)
pairs = []
for i in range(m):
    for j in range(n):
        pairs.append((i, j))
print(pairs)
print(dict(zip(range(1, 10), pairs)))

# A dictionary pairing square numbers as key with tuples, (r,c), as values.
sq = dict(zip(range(1, 10), pairs))


def move(rc, c):
    row = rc[0]
    col = rc[1]
    matrix[row, col] = c


move((1, 1), 1)
move((0, 0), 0)
move(sq[2], 1)
move(sq[3], 0)
move(sq[9], 1)

print(matrix)

