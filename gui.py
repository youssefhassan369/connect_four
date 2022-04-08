import pygame
import sys
import math
Rows = 6
Columns = 7

blue = (0, 0, 255)
black = (0, 0, 0)

SQUARESIZE = 100
Radius=((SQUARESIZE/2)-5)
height = (Rows + 1) * SQUARESIZE
width = Columns * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)

def game(board):
    pygame.init()
    draw_board(board)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                column_number=int(math.floor(x/SQUARESIZE))
                print(column_number) 



def draw_board(board):
    for i in range(0,Columns):
        for j in range(0,Rows):
            pygame.draw.rect(screen, blue, (i*SQUARESIZE, j*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen,black,(int(SQUARESIZE*(i+0.5)), int(SQUARESIZE*(j+1.5))),Radius)