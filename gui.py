import pygame
import sys
from math import inf, floor
from Game import *
from MinMax import *
from AlphaBeta import *
import time

Rows = 6
Columns = 7

blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

SQUARESIZE = 100
Radius = ((SQUARESIZE / 2) - 5)
height = (Rows + 1) * SQUARESIZE
width = Columns * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)


def game(board, mode, k):
    pygame.init()
    myfont = pygame.font.SysFont("monospace", 65)
    draw_board(board)
    pygame.display.flip()
    turn = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if GameEnd(board) == False:
                if turn == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x = event.pos[0]
                        y = event.pos[1]
                        column_number = int(floor(x / SQUARESIZE))
                        flag, result = update_col(board, column_number)
                        if flag:
                            board = Node(0, -inf, inf, result.col0, result.col1, result.col2, result.col3, result.col4,
                                         result.col5, result.col6)
                            turn += 1
                            turn = turn % 2
                            draw_board(board)

                if turn == 0:
                    if mode == 1:
                        t1=time.time()
                        f, count1 = MinMax(board, k, k)
                        t2=time.time()
                        board = Node(0, -inf, inf, f.col0, f.col1, f.col2, f.col3, f.col4, f.col5, f.col6)
                        print("Nodes expanded : ", count1)
                        print("Time = ", t2-t1,"sec")
                        print("")
                        print("")
                        turn += 1
                        turn = turn % 2
                        draw_board(board)
                    if mode == 2:
                        t1=time.time()
                        f, count2 = AlphaBeta(board, k, k)
                        t2 = time.time()
                        board = Node(0, -inf, inf, f.col0, f.col1, f.col2, f.col3, f.col4, f.col5, f.col6)
                        print("Nodes expanded : ", count2)
                        print("Time = ", t2 - t1, "sec")
                        print("")
                        print("")
                        turn += 1
                        turn = turn % 2
                        pygame.display.flip()
                        draw_board(board)
            else:
                user, computer = Score(board)
                label = myfont.render(("Player:" + str(user) + "  AI:" + str(computer)), 1, red)
                screen.blit(label, (40, 10))
                pygame.display.flip()
                draw_board(board)


def draw_board(board):
    total_string = ''.join(reversed(board.col0)) + ''.join(reversed(board.col1)) + ''.join(
        reversed(board.col2)) + ''.join(reversed(board.col3)) + ''.join(reversed(board.col4)) + ''.join(
        reversed(board.col5)) + ''.join(reversed(board.col6))
    step = 6
    for i in range(0, Columns):
        for j in range(0, Rows):
            pygame.draw.rect(screen, blue, (i * SQUARESIZE, j * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if total_string[i * step + j] == 'r':
                pygame.draw.circle(screen, red, (int(SQUARESIZE * (i + 0.5)), int(SQUARESIZE * (j + 1.5))), Radius)
            elif total_string[i * step + j] == 'y':
                pygame.draw.circle(screen, yellow, (int(SQUARESIZE * (i + 0.5)), int(SQUARESIZE * (j + 1.5))), Radius)
            else:
                pygame.draw.circle(screen, black, (int(SQUARESIZE * (i + 0.5)), int(SQUARESIZE * (j + 1.5))), Radius)
    pygame.display.update()


def update_col(board, col):
    if col == 0:
        index = board.col0.find('e')
        if index == -1:
            return False, board
        temp = list(board.col0)
        temp[index] = 'y'
        board.col0 = "".join(temp)
        return True, board

    if col == 1:
        index = board.col1.find('e')
        if index == -1:
            return False, board
        temp = list(board.col1)
        temp[index] = 'y'
        board.col1 = "".join(temp)
        return True, board

    if col == 2:
        index = board.col2.find('e')
        if index == -1:
            return False, board
        temp = list(board.col2)
        temp[index] = 'y'
        board.col2 = "".join(temp)
        return True, board

    if col == 3:
        index = board.col3.find('e')
        if index == -1:
            return False, board
        temp = list(board.col3)
        temp[index] = 'y'
        board.col3 = "".join(temp)
        return True, board

    if col == 4:
        index = board.col4.find('e')
        if index == -1:
            return False, board
        temp = list(board.col4)
        temp[index] = 'y'
        board.col4 = "".join(temp)
        return True, board

    if col == 5:
        index = board.col5.find('e')
        if index == -1:
            return False, board
        temp = list(board.col5)
        temp[index] = 'y'
        board.col5 = "".join(temp)
        return True, board

    if col == 6:
        index = board.col6.find('e')
        if index == -1:
            return False, board
        temp = list(board.col6)
        temp[index] = 'y'
        board.col6 = "".join(temp)
        return True, board
