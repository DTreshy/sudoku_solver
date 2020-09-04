import pygame
from vars import *
from grid import Grid
from math import floor
import numpy as np


class Game:
    grid = Grid()

    def __init__(self):
        while running:
            self.events()
            self.draw()

    def draw(self):
        screen.fill(WHITE)
        self.grid.draw()
        for i in range(0, 11):
            pygame.draw.line(screen, BLACK, (i * WIN_WIDTH / 9, 0), (i * WIN_WIDTH / 9, WIN_WIDTH), 2)
            pygame.draw.line(screen, BLACK, (0, i * WIN_WIDTH / 9), (WIN_WIDTH, i * WIN_WIDTH / 9), 2)
        for i in range(0, 4):
            pygame.draw.line(screen, BLACK, (i * WIN_WIDTH / 3, 0), (i * WIN_WIDTH / 3, WIN_WIDTH), 6)
            pygame.draw.line(screen, BLACK, (0, i * WIN_WIDTH / 3), (WIN_WIDTH, i * WIN_WIDTH / 3), 6)
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vars.running = False
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                col = floor(pos[0] / (WIN_WIDTH / 9) % 9)
                row = floor(pos[1] / (WIN_WIDTH / 9) % 9)
                self.grid.onClick(col, row)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    self.grid.clear()
                if event.key == pygame.K_SPACE:
                    if self.grid.is_full():
                        self.grid.clear()
                    else:
                        self.solve_grid()
                if self.grid.clicked_spot is not None and not self.grid.is_full():
                    key = None
                    if event.key == pygame.K_0:
                        key = 0
                    elif event.key == pygame.K_1:
                        key = 1
                    elif event.key == pygame.K_2:
                        key = 2
                    elif event.key == pygame.K_3:
                        key = 3
                    elif event.key == pygame.K_4:
                        key = 4
                    elif event.key == pygame.K_5:
                        key = 5
                    elif event.key == pygame.K_6:
                        key = 6
                    elif event.key == pygame.K_7:
                        key = 7
                    elif event.key == pygame.K_8:
                        key = 8
                    elif event.key == pygame.K_9:
                        key = 9
                    if key is not None:
                        self.grid.assign_value(key)

    def solve_grid(self):
        for idx, spot in np.ndenumerate(self.grid.grid):
            if spot.value == 0:
                for value in range(1, 10):
                    spot.value = value
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            vars.running = False
                    if self.grid.check_col(spot.col) and self.grid.check_row(spot.row) and self.grid.check_square(spot.square):
                        self.draw()
                        if not self.grid.is_full():
                            if self.solve_grid():
                                return True
                        else:
                            return True
                spot.value = 0
                return False


if __name__ == "__main__":
    game = Game()
    pygame.quit()
