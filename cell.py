from graphics import Line, Point


class Cell:
    def __init__(self, canvas):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = canvas

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        top_left = Point(x1, y1)
        bot_left = Point(x1, y2)
        bot_right = Point(x2, y2)
        top_right = Point(x2, y1)
        if self.has_left_wall:
            left_wall = Line(top_left, bot_left)
            self._win.create_line(left_wall)
        if self.has_top_wall:
            top_wall = Line(top_left, top_right)
            self._win.create_line(top_wall)
        if self.has_right_wall:
            right_wall = Line(top_right, bot_right)
            self._win.create_line(right_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(bot_left, bot_right)
            self._win.create_line(bottom_wall)

    def draw_move(self, to_cell, undo=False):
        if self._x1 is None or self._x2 is None:
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
        self._win.create_line(line, fill_color)
