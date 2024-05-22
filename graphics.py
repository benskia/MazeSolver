from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.wm_protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

    def create_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, pt1, pt2):
        self.pt1 = pt1
        self.pt2 = pt2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, pt1, pt2, canvas):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = pt1.x
        self._y1 = pt1.y
        self._x2 = pt2.x
        self._y2 = pt2.y
        self._win = canvas

    def draw(self, x1, y1, x2, y2):
        if self.has_left_wall:
            pass
