import numpy as np
from spot import Spot
from math import floor


class Grid:
    grid = np.zeros((9, 9), dtype=object)
    clicked_spot = None

    def __init__(self):
        for idx, spot in np.ndenumerate(self.grid):
            self.grid[idx] = Spot(idx[0], idx[1])

    def draw(self):
        for idx, spot in np.ndenumerate(self.grid):
            spot.draw()

    def onClick(self, col, row):
        clicked = self.grid[col, row].clicked
        for idx, spot in np.ndenumerate(self.grid):
            spot.clicked = False
            spot.highlighted = False
        if not clicked:
            self.clicked_spot = (col, row)
            self.grid[col, row].clicked = True
            for i in range(0, 9):
                self.grid[i, row].highlighted = True
                self.grid[col, i].highlighted = True
        else:
            self.clicked_spot = None

    def assign_value(self, value):
        self.grid[self.clicked_spot].value = value

    def is_full(self):
        for idx, spot in np.ndenumerate(self.grid):
            if spot.value == 0:
                return False
        return True

    def check_square(self, square_index):
        square_col = floor(square_index % 3)
        square_row = floor((square_index - square_col) / 3)
        array = np.zeros(9)
        for i in range(3 * square_col, 3 * square_col + 3):
            for j in range(3 * square_row, 3 * square_row + 3):
                if self.grid[i, j].value != 0:
                    if array[self.grid[i, j].value - 1] == 1:
                        return False
                    else:
                        array[self.grid[i, j].value - 1] = 1
        return True

    def check_row(self, row_index):
        array = np.zeros(9)
        for i in range(0, 9):
            if self.grid[i, row_index].value != 0:
                if array[self.grid[i, row_index].value - 1] == 1:
                    return False
                else:
                    array[self.grid[i, row_index].value - 1] = 1
        return True

    def check_col(self, col_index):
        array = np.zeros(9)
        for i in range(0, 9):
            if self.grid[col_index, i].value != 0:
                if array[self.grid[col_index, i].value - 1] == 1:
                    return False
                else:
                    array[self.grid[col_index, i].value - 1] = 1
        return True
