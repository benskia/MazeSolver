from time import sleep
from cell import Cell
from graphics import Window
import random


class Maze:

    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window | None = None,
        seed=None,
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
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int) -> None:
        x1 = (j) * self._cell_size_x + self._x1
        y1 = (i) * self._cell_size_y + self._y1
        x2 = (j + 1) * self._cell_size_x + self._x1
        y2 = (i + 1) * self._cell_size_y + self._y1
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self) -> None:
        last_row_index = self._num_rows - 1
        last_col_index = self._num_cols - 1
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[last_row_index][last_col_index].has_bottom_wall = False
        self._draw_cell(last_row_index, last_col_index)

    def _break_walls(self) -> None:
        self._break_walls_r(0, 0)

    def _break_walls_r(self, i: int, j: int) -> None:
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            can_travel_up = i > 0 and not self._cells[i - 1][j].visited
            can_travel_down = (
                i < self._num_rows - 1 and not self._cells[i + 1][j].visited
            )
            can_travel_left = j > 0 and not self._cells[i][j - 1].visited
            can_travel_right = (
                j < self._num_cols - 1 and not self._cells[i][j + 1].visited
            )
            if can_travel_up:
                to_visit.append((i - 1, j))
            if can_travel_down:
                to_visit.append((i + 1, j))
            if can_travel_left:
                to_visit.append((i, j - 1))
            if can_travel_right:
                to_visit.append((i, j + 1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                break
            next_ij = to_visit[random.randint(0, len(to_visit) - 1)]
            if next_ij[0] < i:
                self._cells[i][j].has_top_wall = False
                self._cells[next_ij[0]][next_ij[1]].has_bottom_wall = False
            if next_ij[0] > i:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_ij[0]][next_ij[1]].has_top_wall = False
            if next_ij[1] < j:
                self._cells[i][j].has_left_wall = False
                self._cells[next_ij[0]][next_ij[1]].has_right_wall = False
            if next_ij[1] > j:
                self._cells[i][j].has_right_wall = False
                self._cells[next_ij[0]][next_ij[1]].has_left_wall = False
            self._break_walls_r(next_ij[0], next_ij[1])

    def _reset_cells_visited(self) -> None:
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False

    def _solve(self) -> bool:
        return self._solve_r(0, 0)

    def _solve_r(self, i, j) -> bool:
        self._animate()
        self._cells[i][j].visited = True
        is_exit_cell = i == self._num_rows - 1 and j == self._num_cols - 1
        if is_exit_cell:
            return True
        can_travel_up = (
            i > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i - 1][j].visited
        )
        can_travel_down = (
            i < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i + 1][j].visited
        )
        can_travel_left = (
            j > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i][j - 1].visited
        )
        can_travel_right = (
            j < self._num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i][j + 1].visited
        )
        if can_travel_up:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            exit_found = self._solve_r(i - 1, j)
            if exit_found:
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        if can_travel_down:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            exit_found = self._solve_r(i + 1, j)
            if exit_found:
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)
        if can_travel_left:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            exit_found = self._solve_r(i, j - 1)
            if exit_found:
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
        if can_travel_right:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            exit_found = self._solve_r(i, j + 1)
            if exit_found:
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
        return False
