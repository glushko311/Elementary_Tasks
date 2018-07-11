
import unittest

from square_sequence import Sequence

class SequenceTestSuit(unittest.TestCase):

    def test_get_n_validate_valid(self):
        res = Sequence.get_n_validate(['any', ['45']])
        self.assertEqual(res.sequence,
                         ['1', '2', '3', '4', '5', '6'])

    def test_get_n_validate_null(self):
        res = Sequence.get_n_validate(['any', ['0']])
        self.assertEqual(res.sequence,
                         [])

    def test_get_n_validate_none(self):
        with self.assertRaises(IndexError):
            Sequence.get_n_validate(['any', []])

    def test_get_n_validate_negative(self):
        with self.assertRaises(ValueError):
            Sequence.get_n_validate(['any', ['-55']])

    def test_get_n_validate_str(self):
        with self.assertRaises(ValueError):
            Sequence.get_n_validate(['any', ['aaa']])

if __name__ == '__main__':
        unittest.main()