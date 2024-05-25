from cell import Cell


class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = self._create_cells()

    def _create_cells(self):
        cells = []
        for i in range(self._num_rows):
            row_cells = []
            for j in range(self._num_cols):
                row_cells.append(Cell(self._win))
            cells.append(row_cells)
        return cells

    def _draw_cell(self, i, j):
        x1 = (j) * self._cell_size_x + self._x1
        y1 = (i) * self._cell_size_y + self._y1
        x2 = (j + 1) * self._cell_size_x + self._x1
        y2 = (i + 1) * self._cell_size_y + self._y1
        self._cells[i][j].draw(x1, y1, x2, y2)
