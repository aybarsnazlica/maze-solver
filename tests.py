import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_start_position(self):
        m2 = Maze(2, 3, 5, 5, 20, 20)

        self.assertEqual(m2._x1, 2)
        self.assertEqual(m2._y1, 3)

    def test_maze_dimensions(self):
        rows, cols = 8, 6
        m3 = Maze(0, 0, rows, cols, 15, 15)

        self.assertEqual(len(m3._cells), cols)

        for col in m3._cells:
            self.assertEqual(len(col), rows)

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )


if __name__ == '__main__':
    unittest.main()
