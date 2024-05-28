from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    
    maze = Maze(50, 50, 5, 7, 100, 100, win, 10)
    maze._break_entrance_and_exit()
    maze._break_walls()
    maze._reset_cells_visited()
    maze._solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
