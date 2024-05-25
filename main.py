from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    
    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(100, 100, 200, 200)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(200, 100, 300, 200)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw(200, 200, 300, 300)

    c4 = Cell(win)
    c4.has_left_wall = False
    c4.draw(300, 200, 400, 300)

    

    win.wait_for_close()


if __name__ == "__main__":
    main()
