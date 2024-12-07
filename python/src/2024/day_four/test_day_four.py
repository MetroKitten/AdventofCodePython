import unittest

from day_four import search_grid


class TestMAS(unittest.TestCase):
    def test_mas_count(self):
        """Test the grid for the correct number of 'MAS' in an X shape."""
        grid = [
            list("MMMSXXMASM"),
            list("MSAMXMSMSA"),
            list("AMXSXMAAMM"),
            list("MSAMASMSMX"),
            list("XMASAMXAMM"),
            list("XXAMMXXAMA"),
            list("SMSMSASXSS"),
            list("SAXAMASAAA"),
            list("MAMMMXMMMM"),
            list("MXMXAXMASX"),
        ]
        result = search_grid(grid)
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
