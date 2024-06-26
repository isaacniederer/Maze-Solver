import unittest

from window import Window

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(1, 1, num_rows, num_cols, 10, 10, Window(800,600))
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(1, 1, num_rows, num_cols, 10, 10, Window(800,600))
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].top_wall,
            False,
        )
        self.assertNotEqual(
            m1._cells[num_cols-1][num_rows-1].bottom_wall,
            True,
        )


if __name__ == "__main__":
    unittest.main()
