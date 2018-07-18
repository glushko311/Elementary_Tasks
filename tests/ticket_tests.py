import unittest

from ticket import Ticket


class TicketTestSuit(unittest.TestCase):
    def test_validate_valid(self):
        res = Ticket.validate('123325')
        self.assertEqual(res, True)

    def test_validate_str(self):
        res = Ticket.validate('aaabbb')
        self.assertEqual(res, False)

    def test_validate_too_long(self):
        res = Ticket.validate('123456789')
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
