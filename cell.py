from graphics import Line, Point, Window


class Cell:
    def __init__(self, win: Window | None = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self._win is None:
            return
        fill_color_white = "white"
        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bot_left = Point(x1, y2)
        bot_right = Point(x2, y2)
        left_wall = Line(top_left, bot_left)
        right_wall = Line(top_right, bot_right)
        top_wall = Line(top_left, top_right)
        bottom_wall = Line(bot_left, bot_right)
        if self.has_left_wall:
            self._win.draw_line(left_wall)
        else:
            self._win.draw_line(left_wall, fill_color_white)
        if self.has_right_wall:
            self._win.draw_line(right_wall)
        else:
            self._win.draw_line(right_wall, fill_color_white)
        if self.has_top_wall:
            self._win.draw_line(top_wall)
        else:
            self._win.draw_line(top_wall, fill_color_white)
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall)
        else:
            self._win.draw_line(bottom_wall, fill_color_white)

    def draw_move(self, to_cell, undo=False):
        if self._x1 is None:
            print("draw_move: x1 is None")
            return
        if self._x2 is None:
            print("draw_move: x2 is None")
            return
        if self._win is None:
            print("draw_move: win is None")
            return
        current_half_length = abs(self._x2 - self._x1) // 2
        current_center_x = self._x1 + current_half_length
        current_center_y = self._y1 + current_half_length
        current_center = Point(current_center_x, current_center_y)

        next_half_length = abs(to_cell._x2 - to_cell._x1) // 2
        next_center_x = to_cell._x1 + next_half_length
        next_center_y = to_cell._y1 + next_half_length
        next_center = Point(next_center_x, next_center_y)
        line = Line(current_center, next_center)
        fill_color = "gray" if undo else "red"
        self._win.draw_line(line, fill_color)
