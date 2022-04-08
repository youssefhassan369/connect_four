from functions import *
from Heuristic import *
from Node import *
from MinMax import *

if __name__ == '__main__':
    board = generateInitialState()
    # print(Heuristic(board))
    MinMax(board, 5, 5)
