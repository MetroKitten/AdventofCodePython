import unittest

from day_five import calc_middle_totals, check_meets_rules


class TestRules(unittest.TestCase):
    def test_check_meet_rules_true(self):
        test_rules = [
            (47, 53),
            (97, 13),
            (97, 61),
            (97, 47),
            (75, 29),
            (61, 13),
            (75, 53),
            (29, 13),
            (97, 29),
            (53, 29),
            (61, 53),
            (97, 53),
            (61, 29),
            (47, 13),
            (75, 47),
            (97, 75),
            (47, 61),
            (75, 61),
            (47, 29),
            (75, 13),
            (53, 13),
        ]
        test_input = [75, 47, 61, 53, 29]
        expected = True
        result = check_meets_rules(test_input, test_rules)
        self.assertEqual(result, expected)

    def test_check_meet_rules_false(self):
        test_rules = [
            (47, 53),
            (97, 13),
            (97, 61),
            (97, 47),
            (75, 29),
            (61, 13),
            (75, 53),
            (29, 13),
            (97, 29),
            (53, 29),
            (61, 53),
            (97, 53),
            (61, 29),
            (47, 13),
            (75, 47),
            (97, 75),
            (47, 61),
            (75, 61),
            (47, 29),
            (75, 13),
            (53, 13),
        ]
        test_input = [75, 97, 47, 61, 53]
        expected = False
        result = check_meets_rules(test_input, test_rules)
        self.assertEqual(result, expected)

    def test_check_list_total(self):
        test_list = [75, 47, 61, 53, 29]
        expected = 61
        result = calc_middle_totals(test_list)
        self.assertEqual(result, expected)
