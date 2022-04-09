from Game import *
from gui import *

if __name__ == '__main__':
    # print('Select the mode you want to play')
    # print('1) Minimax without alpha-beta pruning')
    # print('2) Minimax without alpha-beta pruning')
    # mode = input('mode: ')
    # print('Enter Number of levels (k):')
    # levels = input('levels: ')

    board = generateInitialState()

    game(board,1,3)

