import unittest

from file_handler import FileHandler

from ticket import Ticket
from ticket_handler import TicketHandler

class TicketHandlerTestSuit(unittest.TestCase):

    def test_validate_valid(self):
        handler = TicketHandler()
        handler.generate_tickets_by_input_numbers(1, 2)
        res = handler.tickets
        self.assertEqual(res, [Ticket('000001'), Ticket('000002')])

    def test_validate_valid2(self):
        handler = TicketHandler()
        handler.generate_tickets_by_input_numbers(777000, 777002)
        self.assertEqual(handler.tickets, [Ticket('777000'), Ticket('777001'), Ticket('777002')])

    def test_validate_valid3(self):
        handler = TicketHandler()
        handler.generate_tickets_by_input_numbers(0, 1)
        self.assertEqual(handler.tickets, [Ticket('000000'), Ticket('000001')])

    def test_set_algorithm_mosk(self):
        handler = TicketHandler()
        handler.set_algorithm('blablabvla Moscow blablabvla')
        self.assertEqual(handler.algorithm, 'Moscow')

    def test_set_algorithm_piter(self):
        handler = TicketHandler()
        handler.set_algorithm('bla blabvla Piter blablabv la123')
        self.assertEqual(handler.algorithm, 'Piterburg')

    def test_count_happy_tickets_mosk(self):
        handler = TicketHandler()
        handler.generate_tickets_by_input_numbers(111111, 222222)
        handler.set_algorithm('Moscow')
        handler.count_happy_tickets()
        self.assertEqual(handler.count, 5802)

    def test_count_happy_tickets_piter(self):
        handler = TicketHandler()
        handler.generate_tickets_by_input_numbers(111111, 222222)
        handler.set_algorithm('Piter')
        handler.count_happy_tickets()
        self.assertEqual(handler.count, 5986)

    def test_count_happy_tickets_all_piter(self):
        handler = TicketHandler()
        handler.set_algorithm('Piter')
        handler.count_happy_tickets(True)
        self.assertEqual(handler.count, 55252)

    def test_count_happy_tickets_all_moscow(self):
        handler = TicketHandler()
        handler.set_algorithm('Moscow')
        handler.count_happy_tickets(True)
        self.assertEqual(handler.count, 55252)


if __name__ == '__main__':
        unittest.main()