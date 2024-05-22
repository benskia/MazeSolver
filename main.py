from graphics import Window, Point
from cell import Cell


def main():
    win = Window(800, 600)
    pt1 = Point(100, 100)
    pt2 = Point(200, 200)
    pt3 = Point(200, 100)
    pt4 = Point(300, 200)
    cell1 = Cell(pt1, pt2, win)
    cell2 = Cell(pt3, pt4, win)
    cell1.draw(pt1.x, pt1.y, pt2.x, pt2.y)
    cell2.draw(pt3.x, pt3.y, pt4.x, pt4.y)
    win.wait_for_close()


if __name__ == "__main__":
    main()
