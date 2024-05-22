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
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        top_left = Point(x1, y1)
        bot_left = Point(x1, y2)
        top_right = Point(x2, y1)
        bot_right = Point(x2, y2)
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
