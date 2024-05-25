from graphics import Window
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    
    maze = Maze(10, 10, 4, 4, 100, 100, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
