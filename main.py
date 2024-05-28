from graphics import Window
from maze import Maze


def main():
    win = Window(1000, 800)
    
    maze = Maze(50, 50, 7, 9, 100, 100, win)
    maze._break_entrance_and_exit()
    maze._break_walls()
    maze._reset_cells_visited()
    maze._solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
