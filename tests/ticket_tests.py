import unittest
import os
from unittest import mock

from file_handler import FileHandler
from ticket import Ticket


class TicketTestSuit(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=['123325'])
    def test_get_n_validate_valid(self, input):
        res = Ticket.get_n_validate()
        self.assertEqual(res, True)

    @mock.patch('builtins.input', side_effect=['aaabbb'])
    def test_get_n_validate_str(self, input):
        res = Ticket.get_n_validate()
        self.assertEqual(res, False)

    @mock.patch('builtins.input', side_effect=['123456789'])
    def test_get_n_validate_too_long(self, input):
        res = Ticket.get_n_validate()
        self.assertEqual(res, False)

    def test_is_happy_mosk_true(self):
        ticket = Ticket('123321')
        mark = "Moscow"
        self.assertEqual(ticket.is_happy(mark), True)

    def test_is_happy_mosk_true2(self):
        ticket = Ticket('777777')
        mark = "Moscow"
        self.assertEqual(ticket.is_happy(mark), True)

    def test_is_happy_mosk_false(self):
        ticket = Ticket('128321')
        mark = "Moscow"
        self.assertEqual(ticket.is_happy(mark), False)


    def test_is_happy_piter_true(self):
        ticket = Ticket('113322')
        mark = "Piterburg"
        self.assertEqual(ticket.is_happy(mark), True)

    def test_is_happy_piter_true2(self):
        ticket = Ticket('777777')
        mark = "Piterburg"
        self.assertEqual(ticket.is_happy(mark), True)

    def test_is_happy_piter_false(self):
        ticket = Ticket('128321')
        mark = "Piterburg"
        self.assertEqual(ticket.is_happy(mark), False)




if __name__ == '__main__':
        unittest.main()