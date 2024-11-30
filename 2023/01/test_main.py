import unittest

from main import Calibration, CalibrationV2


class TestCalibration(unittest.TestCase):
    def test_Calibration(self):
        input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        expected = 142
        output = Calibration(input)
        self.assertEqual(output, expected)

    def test_CalibrationV2(self):
        input = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]
        expected = 281
        output = CalibrationV2(input)
        self.assertEqual(output, expected)
