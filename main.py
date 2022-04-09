from AlphaBeta import AlphaBeta
from functions import *
from Heuristic import *
from Node import *
from MinMax import *
from gui import *

if __name__ == '__main__':
    board = generateInitialState()

    #print(Heuristic(board))
    #MinMax(board, 5, 5)
    game(board,1)
    #print(Heuristic(board))
    #MinMax(board, 5, 5)
   # AlphaBeta(board,5,5)
