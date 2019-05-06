# Create a function ListGames(r,c) that generates a file with all possible "games."   A "game" is a board completely filled with x's and o's such that the number of x's is either equal to the number o's or greater by 1 depending on whether there are an even or odd number of squares.   This functions will be useful for finding won and drawn games.   We can use the list for later attempts at machine learning.

# This will result in 2^(m x n) "games."  That should be small enough assuming r x c is <= 25.

# This list will not list all of the games since the order of play makes a difference in a game.   Also a game ends when either player gets n in a row.

import numpy as np

def ListGames(r, c):
  # r is the number rows and c is the number of column in the board.
  
  # code ...
