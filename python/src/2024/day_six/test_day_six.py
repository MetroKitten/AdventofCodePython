import unittest

from day_six import *


class TestGuardRoute(unittest.TestCase):
    def test_mas_count(self):
        """Test the grid for the correct number of 'MAS' in an X shape."""
        grid = [
            [".", ".", ".", ".", "#", ".", ".", ".", "."],
            [".", ".", ".", ".", "^", ".", ".", ".", "#"],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "#", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "#", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "#", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", "."],
            ["#", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "#", ".", "."],
        ]

        result = search_grid(grid)
        self.assertEqual(result, 41)


if __name__ == "__main__":
    unittest.main()
