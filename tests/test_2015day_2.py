import unittest

from year2015.solutions.day_2 import part_1, part_2


class Part_1_test(unittest.TestCase):
    def test_1(self):
        result = part_1("year2015/inputs/day_2/part_1_test_1.txt")
        self.assertEqual(result, 58)


class Part_2_test(unittest.TestCase):
    def test_1(self):
        result = part_2("year2015/inputs/day_2/part_2_test_1.txt")
        self.assertEqual(result, 34)

    def test_2(self):
        result = part_2("year2015/inputs/day_2/part_2_test_puzzle_inp.txt")
        print(result)
        # self.assertEqual(result, 34)
