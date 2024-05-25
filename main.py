from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    
    c = Cell(win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
