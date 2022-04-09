from AlphaBeta import AlphaBeta
from functions import *
from Heuristic import *
from Node import *
from MinMax import *
from gui import *
from AlphaBeta import *
from math import inf

if __name__ == '__main__':
    # print('Select the mode you want to play')
    # print('1) Minimax without alpha-beta pruning')
    # print('2) Minimax without alpha-beta pruning')
    # mode = input('mode: ')
    # print('Enter Number of levels (k):')
    # levels = input('levels: ')

    board = generateInitialState()

    #print(Heuristic(board))
    #temp=MinMax(board, 3, 3)
    #print(temp.col3)
    print(inf)

    game(board,2,4)

    #print(Heuristic(board))
    #res,tree=MinMax(board, 5, 5)
    #AlphaBeta(board,5,5)
