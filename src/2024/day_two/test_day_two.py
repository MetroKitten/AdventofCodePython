import unittest

from day_two import safety_report


class SafetyReportTest(unittest.TestCase):
    def test_safety_report1(self):
        reports = [7, 6, 4, 2, 1]
        expected = True
        output = safety_report(reports)
        self.assertEqual(output, expected)

    def test_safety_report2(self):
        reports = [1, 2, 7, 8, 9]
        expected = False
        output = safety_report(reports)
        self.assertEqual(output, expected)

    def test_safety_report3(self):
        reports = [9, 7, 6, 2, 1]
        expected = False
        output = safety_report(reports)
        self.assertEqual(output, expected)

    def test_safety_report4(self):
        reports = [1, 3, 2, 4, 5]
        expected = False
        output = safety_report(reports)
        self.assertEqual(output, expected)

    def test_safety_report5(self):
        reports = [8, 6, 4, 4, 1]
        expected = False
        output = safety_report(reports)
        self.assertEqual(output, expected)

    def test_safety_report6(self):
        reports = [1, 3, 6, 7, 9]
        expected = True
        output = safety_report(reports)
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
