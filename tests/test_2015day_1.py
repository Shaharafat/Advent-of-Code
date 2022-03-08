import unittest

from year2015.solutions.day_1 import part_1, part_2


class Test_day_1(unittest.TestCase):
  def test_part_1_first(self):
    filename = 'year2015/inputs/day_1/first.txt'

    result = part_1(filename)
    self.assertEqual(result, 0)


  def test_part_1_second(self):
    filename = 'year2015/inputs/day_1/second.txt'

    result = part_1(filename)
    self.assertEqual(result, 3)

  def test_part_1_third(self):
    filename = 'year2015/inputs/day_1/third.txt'

    result = part_1(filename)
    self.assertEqual(result, 3)

  def test_part_1_fourth(self):
    filename = 'year2015/inputs/day_1/fourth.txt'

    result = part_1(filename)
    self.assertEqual(result, -1)

  def test_part_1_fifth(self):
    filename = 'year2015/inputs/day_1/fifth.txt'

    result = part_1(filename)
    self.assertEqual(result, -3)

  def test_part_1_sixth(self):
    filename = 'year2015/inputs/day_1/sixth.txt'

    result = part_1(filename)
    print(result)

  

  def test_part_2_first(self):
    filename = 'year2015/inputs/day_1/part_2_first.txt'

    result = part_2(filename)
    self.assertEqual(result, 1)

  def test_part_2_second(self):
    filename = 'year2015/inputs/day_1/part_2_second.txt'

    result = part_2(filename)
    self.assertEqual(result, 5)

  def test_part_2_third(self):
    filename = 'year2015/inputs/day_1/part_2_third.txt'

    result = part_2(filename)
    # self.assertEqual(result, -3)
    print(result)
