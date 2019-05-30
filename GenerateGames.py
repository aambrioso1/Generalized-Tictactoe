# This program will generate games on a board.   The idea is to indicate moves by alternating square numbers.
# I would like to modify it so that it could steps through each games in the list of games for r x c board.

import numpy as np
from itertools import permutations
# We use the print_mat function in the MatrixPrint module.
# I need to create a library call tictactoeTools
# import tictactoeTools as ttt

def print_mat(m):
    s = [[str(e) for e in row] for row in m]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

rows = 3
columns = 3
r = rows
c = columns


# Make a list with stones on appropriate squares.
# for i in range(9):
    #print(list1[9][i])
bd = np.array([None,None,None,None,None,None,None,None,None])
bd.shape = (r,c)
print(f"This is the blank board\n{bd}")


# These dictionaries are used to convert square numbers to tuples with the appropriate row and column.
# This is for a 3 x 3 board only.
sq = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}
inv_sq = {(0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 7, (2, 1): 8, (2, 2): 9}


"""
This code is used to generate the two dictionaries sq and inv_sq.  I will need it when a generalize the program.
pairs = []
for i in range(m):
    for j in range(n):
        pairs.append((i, j))
print(pairs)
print(dict(zip(range(1, 10), pairs)))

# Need to generalize and automate the construction of this dictionary with zip().
sq = dict(zip(range(1, 10), pairs))
inv_sq = dict(zip(sq.values(), sq.keys()))

"""

#  List one contains every permutation of the characters in the string 123456789.
#  Each strings represent a tictactoe game if players continued to play until the board was full.
list1= list(permutations('123456789'))
print(f"The number of games possible is {len(list1)} which should equal 9! = {len(list1)}")


# Now we need to take each one of these lists and place each stone on the board alternating stone colors.

# This function takes an tuple(row, column) and places and stone (0, 1, None) on the board bd(global)
def move(rc, s):
    row = rc[0]
    col = rc[1]
    bd[row, col] = s


# Make a list with stones on appropriate squares.
# for i in range(9):
    #print(list1[9][i])



def move(rc, s):
    row = rc[0]
    col = rc[1]
    bd[row, col] = s
    return bd


#  Need to fix move() function

for i in range(50):
    for j in range(9):
        play = int(list1[i][j])
        if j%2 == 0:
            move(sq[play], 1)
        if j%2 == 1:
            move(sq[play], 0)
    print(f"\nThis is game {i+1}: {list1[i]}")
    print_mat(bd)
    # ttt.print_mat(bd)
