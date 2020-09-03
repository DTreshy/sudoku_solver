import pygame
import os

pygame.init()
CAPTION = "Sudoku Solver"
pygame.display.set_caption(CAPTION)
pygame.font.init()
font1 = pygame.font.Font('fonts/Roboto.ttf', 60)
WIN_HEIGHT = 750
WIN_WIDTH = 750
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
running = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (25, 118, 210)
LIGHTBLUE = (3, 169, 244)
