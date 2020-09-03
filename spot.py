from vars import *
from math import floor


class Spot:
    value = 0
    clicked = False
    highlighted = False
    locked = False

    def __init__(self, col, row):
        self.row = row
        self.col = col
        self.square = floor((col / 3)) + 3 * floor((row / 3))

    def draw(self):
        color = WHITE
        if self.highlighted:
            color = LIGHTBLUE
        if self.clicked:
            color = BLUE
        pygame.draw.rect(screen, color, [WIN_WIDTH / 9 * self.col, WIN_WIDTH / 9 * self.row, WIN_WIDTH / 9, WIN_WIDTH / 9])
        if self.value != 0:
            text = font1.render(str(self.value), False, BLACK)
            screen.blit(text, (WIN_WIDTH / 9 * self.col + 25, WIN_WIDTH / 9 * self.row + 8))
