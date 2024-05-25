from graphics import Line, Point


class Cell:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = canvas

    def draw(self):
        top_left = Point(self._x1, self._y1)
        bot_left = Point(self._x1, self._y2)
        bot_right = Point(self._x2, self._y1)
        top_right = Point(self._x2, self._y2)
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
        if [v is None for v in [self._x1, self._y1, self._x2, self._y2]]:
            return
        current_center_x = self._x1 + (self._x2 - self._x1) // 2
        current_center_y = self._y1 + (self._y2 - self._y1) // 2
        current_center = Point(current_center_x, current_center_y)
        next_center_x = to_cell._x1 + (to_cell._x2 - to_cell._x1) // 2
        next_center_y = to_cell._y1 + (to_cell._y2 - to_cell._y1) // 2
        next_center = Point(next_center_x, next_center_y)
        line = Line(current_center, next_center)
        fill_color = "gray" if undo else "red"
        line.draw(self._win, fill_color)
