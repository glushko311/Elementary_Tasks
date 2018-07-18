
import unittest
# from unittest import mock

from triangular import Triangular
from exceptions.triangular_exception import TriangularException


class TriangularTestSuit(unittest.TestCase):
    # @mock.patch('builtins.input', side_effect=['name,5,6,7'])
    # def test_get_n_validate_valid(self, input):
    #     res = Triangular.get_n_validate()
    #     self.assertEqual(res, Triangular(5, 6, 7, 14.7, 'name'))

# Test triangular sort

    def test_triangular_sort(self):
        triang1 = Triangular(3, 4, 5, 6, "name1")
        triang2 = Triangular(1, 2, 1.3, 0.56, "name2")
        triang3 = Triangular(5, 5, 6, 12, "name3")

        arr = [triang1, triang2, triang3]
        expected_res = [triang3, triang1, triang2]
        actual_res = Triangular.sort_triangular_list(arr)

        self.assertEqual(expected_res[0], actual_res[0])
        self.assertEqual(expected_res[1], actual_res[1])
        self.assertEqual(expected_res[2], actual_res[2])


if __name__ == '__main__':
        unittest.main()