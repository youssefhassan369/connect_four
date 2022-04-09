from AlphaBeta import AlphaBeta
from functions import *
from Heuristic import *
from Node import *
from MinMax import *
from gui import *
from AlphaBeta import *

if __name__ == '__main__':
    board = generateInitialState()

    #print(Heuristic(board))
    #temp=MinMax(board, 3, 3)
    #print(temp.col0)
    game(board,1)
    #print(Heuristic(board))
    #res,tree=MinMax(board, 5, 5)
    #AlphaBeta(board,5,5)
