# This program will generate games on a board.   The idea is to indicate moves by alternating square numbers.
# The goal is two create to functions one that generates all possible complete games on r x c board and another
# that takes a game listed as square numbers and place the move on the board one move at a time.

import numpy as np
from itertools import permutations, islice
# We use the print_mat function in the MatrixPrint module.
# I need to create a library call tictactoeTools
# import tictactoeTools as ttt


def print_mat(m):
    s = [[str(e) for e in row] for row in m]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


rows = 4
columns = 4

r = rows
c = columns
rxc = r*c

# We create an r x c board initials with None.  Note that "None" represents an empty square.
empty_bd = np.full((r, c), None)
bd = np.full((r, c), None)
print(f"This is the blank board\n{bd}")

"""
# These dictionaries are used to convert square numbers to tuples and vice versa with the appropriate row and column.
# This is for a 3 x 3 board only.
sq = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}
inv_sq = {(0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 7, (2, 1): 8, (2, 2): 9}
"""

# This code is used to generate the two dictionaries sq and inv_sq.  I will need it when a generalize the program.
pairs = []
for i in range(r):
    for j in range(c):
        pairs.append((i, j))

# Need to generalize and automate the construction of this dictionary with zip().
sq = dict(zip(range(1, rxc+1), pairs))
inv_sq = dict(zip(sq.values(), sq.keys()))

print(f"\nHere is the sq dictionary: {sq}")


#  List one contains every permutation of the characters in the string 123456789.
#  Each strings represent a tictactoe game if players continued to play until the board was full.

list1 = permutations([str(i) for i in range(1, rxc+1)])


# Now we need to take each one of these lists and place each stone on the board alternating stone colors as we do.

# This function takes an tuple(row, column) and places and stone (0, 1, None) on the board bd(global)
def move(rc, s):
    row = rc[0]
    col = rc[1]
    bd[row, col] = s


# Make a list with stones on appropriate squares.
# for i in range(9):
#   print(list1[9][i])

#  Need create functions:  GenerateGames(r,c,num) and PlayGame(r,c,movelist)


for i in islice(list1,5):
    for j in range(rxc):
        play = int(i[j])
        if j%2 == 0:
            move(sq[play], 1)
        if j%2 == 1:
            move(sq[play], 0)
    print(f"Games: {i}\n{bd}")


bd = empty_bd
"""
print(f"Here is {list1[0]} played out:")
for j in range(0, rxc):
    play = int(list1[0][j])
    if j % 2 == 0:
        move(sq[play], 1)
    if j % 2 == 1:
        move(sq[play], 0)
    print(bd)
"""
# print(f"\nThis is game {i+1}: {list1[i]}")
# print_mat(bd)
# ttt.print_mat(bd)
