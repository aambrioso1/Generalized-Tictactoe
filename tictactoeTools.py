# A library of functions useful for working with the data structures associated with the generalized tic-tac-toe project.

# def createboard(m, n)
# creates an empty m x n array

# Prints out out the nicely.
def printboard(board):
    s = [[str(e) for e in row] for row in board]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

# move(mark, board, square)
# places mark on the board at square

# countneighbors(board, square)
# counts how many neighbors of square are x’s, o’s, or empty.

# In_a_Row(mark, board, square)
# Computes the number of marks in a row connected to square.
# Returns a tuple (hor, vert, diag down, diag up)

# Need to think about creating a class called board.
