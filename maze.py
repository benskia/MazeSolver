from time import sleep
from cell import Cell
import random


class Maze:

    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        if seed:
            random.seed(seed)

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_rows):
            row_cells = []
            for j in range(self._num_cols):
                row_cells.append(Cell(self._win))
            self._cells.append(row_cells)
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = (j) * self._cell_size_x + self._x1
        y1 = (i) * self._cell_size_y + self._y1
        x2 = (j + 1) * self._cell_size_x + self._x1
        y2 = (i + 1) * self._cell_size_y + self._y1
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        last_row = len(self._cells) - 1
        last_col = len(self._cells[-1]) - 1
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[last_row][last_col].has_bottom_wall = False
        self._draw_cell(last_row, last_col)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            prev_row = i-1 if i > 0 else i
            next_row = i+1 if i < len(self._cells) - 1 else i
            prev_col = j-1 if i > 0 else j
            next_row = j+1 if j < len(self._cells[i]) - 1 else j
