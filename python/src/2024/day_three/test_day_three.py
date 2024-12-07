import unittest

from day_three import find_muls


class TestCalculation(unittest.TestCase):
    def test_mul_detection1(self):
        input = (
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        )
        expected = 161
        output = find_muls(input)
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
