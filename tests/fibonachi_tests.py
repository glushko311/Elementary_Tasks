import unittest
from fibonachi import Fibonachi


class FibonachiTestList(unittest.TestCase):
    def test_regular(self):
        res = Fibonachi.fib_in_interval(0, 25)
        self.assertEqual(res, [0, 1, 1, 2, 3, 5, 8, 13, 21])

    def test_empty(self):
        res = Fibonachi.fib_in_interval(0, 0)
        self.assertEqual(res, [0])

    def test_from_border(self):
        res = Fibonachi.fib_in_interval(8, 21)
        self.assertEqual(res, [8, 13, 21])

    def test_from(self):
        res = Fibonachi.fib_in_interval(6, 18)
        self.assertEqual(res, [8, 13])

if __name__ == '__main__':
        unittest.main()