from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    
    maze = Maze(50, 50, 5, 7, 100, 100, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
