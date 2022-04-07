from functions import *
from Heuristic import *

if __name__ == '__main__':
    board=generateInitialState()
    print(Heuristic(board))