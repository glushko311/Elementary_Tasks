import unittest
from unittest import mock

from envelope import Envelope


class EnvelopeTestList(unittest.TestCase):
    def test_not_into1(self):
        env1 = Envelope(4, 4)
        env2 = Envelope(1, 7)
        res = Envelope.is_into(env1, env2)
        self.assertEqual(res[0], env2)
        self.assertEqual(res[1], env1)
        self.assertEqual(res[2], False)

    def test_not_into2(self):
        env1 = Envelope(5, 4)
        env2 = Envelope(5.3, 3)
        res = Envelope.is_into(env1, env2)
        self.assertEqual(res[0], env2)
        self.assertEqual(res[1], env1)
        self.assertEqual(res[2], False)

    def test_is_into1(self):
        env1 = Envelope(4, 4)
        env2 = Envelope(2, 2)
        res = Envelope.is_into(env1, env2)
        self.assertEqual(res[0], env2)
        self.assertEqual(res[1], env1)
        self.assertEqual(res[2], True)

    def test_is_into2(self):
        env1 = Envelope(5, 4)
        env2 = Envelope(5.1, 1)
        res = Envelope.is_into(env1, env2)
        self.assertEqual(res[0], env2)
        self.assertEqual(res[1], env1)
        self.assertEqual(res[2], True)

    def test_is_into_reverce(self):
        env1 = Envelope(5.1, 1)
        env2 = Envelope(4, 5)
        res = Envelope.is_into(env1, env2)
        self.assertEqual(res[0], env1)
        self.assertEqual(res[1], env2)
        self.assertEqual(res[2], True)

    def test_is_into1_reverce(self):
        env1 = Envelope(4.9, 3.9)
        env2 = Envelope(4, 5)
        res = Envelope.is_into(env1, env2)
        self.assertEqual(res[0], env1)
        self.assertEqual(res[1], env2)
        self.assertEqual(res[2], True)

    @mock.patch('builtins.input', side_effect=['14', '13'])
    def test_get_n_validate_int(self, input):
        res = Envelope.get_n_validate()
        self.assertEqual(res, Envelope(14, 13))

    @mock.patch('builtins.input', side_effect=['2.6765', '4.787'])
    def test_get_n_validate_float(self, input):
        res = Envelope.get_n_validate()
        self.assertEqual(res, Envelope(2.6765, 4.787))

    @mock.patch('builtins.input', side_effect=['0', '0'])
    def test_get_n_validate_null(self, input):
        with self.assertRaises(ValueError):
            Envelope.get_n_validate()

    @mock.patch('builtins.input', side_effect=['a', 'b'])
    def test_get_n_validate_string(self, input):
        with self.assertRaises(ValueError):
            Envelope.get_n_validate()

    @mock.patch('builtins.input', side_effect=['-5', '5'])
    def test_get_n_validate_negative(self, input):
        with self.assertRaises(ValueError):
            Envelope.get_n_validate()

    @mock.patch('builtins.input', side_effect=['5', 'b'])
    def test_get_n_validate_string2(self, input):
        with self.assertRaises(ValueError):
            Envelope.get_n_validate()

    @mock.patch('builtins.input', side_effect=['5a', '4'])
    def test_get_n_validate_string3(self, input):
        with self.assertRaises(ValueError):
            Envelope.get_n_validate()


if __name__ == '__main__':
        unittest.main()