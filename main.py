from ticket_handler import TicketHandler


def start():
    '''
    Start application function
    :return:
    '''
    handler = TicketHandler()
    if handler.input_mark() == "quit":
        quit()
    if handler.tickets_input() == "quit":
        quit()
    handler.print_counting_result()

start()
