import unittest

from day_one import similarity_score, total_distance


class TotalDistanceTest(unittest.TestCase):
    def test_TotalDistanceCheck(self):
        left_list = [3, 4, 2, 1, 3, 3]
        right_list = [4, 3, 5, 3, 9, 3]
        expected = 11
        output = total_distance(left_list, right_list)
        self.assertEqual(output, expected)

    def test_similarityscore(self):
        left_list = [3, 4, 2, 1, 3, 3]
        right_list = [4, 3, 5, 3, 9, 3]
        expected = 31
        output = similarity_score(left_list, right_list)
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
