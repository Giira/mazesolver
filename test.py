import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_cell_creation(self):
        num_cols = 30
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1.cells), num_cols)
        self.assertEqual(len(m1.cells[0]), num_rows)

    def test_visit_reset(self):
        num_cols = 14
        num_rows = 11
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(False, m1.cells[0][0].visited)

if __name__ == "__main__":
    unittest.main()
