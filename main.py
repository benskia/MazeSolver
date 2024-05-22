from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    
    c = Cell(win)
    c.has_right_wall = False
    c.draw(100, 100, 200, 200)

    c = Cell(win)
    c.has_left_wall = False
    c.has_bottom_wall = False
    c.draw(200, 100, 300, 200)

    c = Cell(win)
    c.has_top_wall = False
    c.has_right_wall = False
    c.draw(200, 200, 300, 300)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(300, 200, 400, 300)

    win.wait_for_close()


if __name__ == "__main__":
    main()
