import unittest

from main import Calibration


class TestCalibration(unittest.TestCase):
    def test_Calibration(self):
        input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        expected = 142
        output = Calibration(input)
        self.assertEqual(output, expected)
