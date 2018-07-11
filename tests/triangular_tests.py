
import unittest
from unittest import mock

from triangular import Triangular
from triangular_exception import TriangularException


class TriangularTestSuit(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=['name,5,6,7'])
    def test_get_n_validate_valid(self, input):
        res = Triangular.get_n_validate()
        self.assertEqual(res, Triangular(5, 6, 7, 14.7, 'name'))

    @mock.patch('builtins.input', side_effect=['name,3,4,5'])
    def test_get_n_validate_square(self, input):
        res = Triangular.get_n_validate()
        self.assertEqual(res.square, 6)

    @mock.patch('builtins.input', side_effect=['name,5.3456,6.7,7.2'])
    def test_get_n_validate_float(self, input):
        res = Triangular.get_n_validate()
        self.assertEqual(res, Triangular(5.3456, 6.7, 7.2, 17.07, 'name'))

    @mock.patch('builtins.input', side_effect=['name,a,6,7'])
    def test_get_n_validate_str(self, input):
        with self.assertRaises(ValueError):
            Triangular.get_n_validate()

    @mock.patch('builtins.input', side_effect=[''])
    def test_get_n_validate_blank_input(self, input):
        with self.assertRaises(TriangularException):
            Triangular.get_n_validate()

    @mock.patch('builtins.input', side_effect=['name,1,56,7'])
    def test_get_n_validate_imposible_triang(self, input):
        with self.assertRaises(TriangularException):
            Triangular.get_n_validate()

    @mock.patch('builtins.input', side_effect=['name'])
    def test_get_n_validate_inv_sides(self, input):
        with self.assertRaises(IndexError):
            Triangular.get_n_validate()

    @mock.patch('builtins.input', side_effect=['name, 0, 0, 0'])
    def test_get_n_validate_null_triang(self, input):
        with self.assertRaises(TriangularException):
            Triangular.get_n_validate()

    @mock.patch('builtins.input', side_effect=['name, -5, -4, -6'])
    def test_get_n_validate_negative_sides(self, input):
        with self.assertRaises(TriangularException):
            Triangular.get_n_validate()

    @mock.patch('builtins.input', side_effect=['name,,,'])
    def test_get_n_validate_without(self, input):
        with self.assertRaises(ValueError):
            Triangular.get_n_validate()

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