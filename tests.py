import unittest
from maze import Maze


class Test(unittest.TestCase):

    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_break_entrance_and_exit(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        last_row = len(m1._cells) - 1
        last_col = len(m1._cells[-1]) - 1
        m1._break_entrance_and_exit()
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[last_row][last_col].has_bottom_wall, False)


if __name__ == "__main__":
    unittest.main()
