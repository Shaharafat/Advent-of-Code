import unittest

from year2015.solutions.day_2 import part_1


class Part_1_test(unittest.TestCase):
    def test_1(self):
        result = part_1("year2015/inputs/day_2/part_1_test_1.txt")
        self.assertEqual(result, 58)
