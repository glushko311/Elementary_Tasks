from os.path import exists

from ticket import Ticket
from validator import Validator
from task_validator import TaskValidator


class TicketHandler(object):
    """
    Singleton class can get user data, validate and save them as tickets
    can calculate how many happy tickets it's contain
    """
    PITER_ALGORITHM_MARK = "Piterburg"
    MOSCOW_ALGORITHM_MARK = "Moscow"

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self):
        self.__algorithm = ""
        self.__tickets = []
        self.__count = 0

    def input_mark(self):
        """
        Get path to file with mark of type calculation happy
        ticket( Moscow or Pitersburg types are available)
        and put method name for calculate happy tickets
        into ___algorithm
        for test use:
        'data/piter.txt' - file with mark of St.Pitersburg method
        'data/mosk.txt' - file with mark of Moscow method
        :return text:
        """
        flag = True
        while flag:
            path = input("Input path to file with mark of algorithm - ")
            # path = "data/mosk.txt"
            validate_res = Validator.single_validate({"value": path,
                                                      "rules": ("file_exists",)})
            if not validate_res[0]:
                print(validate_res[1])
                flag = self.do_continue()
                continue
            with open(path, 'r') as f:
                text = f.read()
            if text.find('Moscow') != -1 and text.find('Piter') != -1:
                print("It seems we have two keys in single file:\n"
                      "You need input path to file with only one key")
                continue
            elif text.find('Moscow') == -1 and text.find('Piter') == -1:
                print("It seems it is no any key in your file:\n"
                      "you need key \"Piter\" or \"Moscow\"")
                continue
            else:
                flag = False
                self.set_algorithm(text)
        return self.algorithm != ""

    def set_algorithm(self, text):
        """
        Find algorithm mark in text and set it into self.__algorithm
        :param text:
        :return:
        """
        if text.find("Moscow") != -1:
            self.__algorithm = __class__.MOSCOW_ALGORITHM_MARK
        elif text.find("Piter") != -1:
            self.__algorithm = __class__.PITER_ALGORITHM_MARK

    @staticmethod
    def do_continue():
        """
        Get user input and check is it y or YES return True/False
        :return: Bool
        """
        want_continue = (input("Would you like to continue \'y\' or \'Yes\'")).upper()
        if want_continue in ('Y', 'YES'):
            return True
        else:
            return False

    def get_tickets_from_file(self):
        """
        Get filepath from console validate and get
        tickets from file and save they into self.__tickets
        :return: None
        """
        is_continue = True
        while is_continue:
            file_path = input("Input path to file with tickets - ")
            validate_res = TaskValidator.validate_tickets_file(file_path)
            if validate_res[0]:
                with open(file_path, "r") as f:
                        tickets = f.read()
                for t in tickets.split(','):
                    self.__tickets.append(Ticket(t))
                print("Tickets loaded successfully!")
                is_continue = False
            else:
                print(validate_res[1])
                is_continue = __class__.do_continue()

    def input_tickets_manually(self):
        """
        Get tickets from console(user input) validate and
        save they into self.__tickets
        :return: None
        """
        flag = True
        while flag:
            print("Input ticket number - 6 digits:")
            ticket_num = input()
            validation_res = TaskValidator.validate_ticket(ticket_num)
            if validation_res[0]:
                self.__tickets.append(Ticket(ticket_num))
            else:
                print(validation_res[1])
            flag = self.do_continue()

    def get_tickets_from_numbers(self):
        """
        Get min and max ticket value from console(user input) validate and
        generate tickets between min and max, save they into self.__tickets
        :return: None
        """
        flag = True
        while flag:

            print("Input minimum ticket number between 000000 .. 999999:")
            minimum_num = input()
            print("Input maximum ticket number between 000000 .. 999999:")
            maximum_num = input()
            validate_res = TaskValidator.validate_tickets_from_numbers(minimum_num, maximum_num)
            if validate_res[0]:
                self.generate_tickets_by_input_numbers(int(minimum_num), int(maximum_num))
                flag = False
            else:
                print(validate_res[1])
                flag = __class__.do_continue()

    def generate_tickets_by_input_numbers(self, minimum_num: int, maximum_num: int):
        """
        Generate list of tickets between minimum_num and maximum_num
        Put list into self.__tickets
        :param minimum_num:
        :param maximum_num:
        :return:
        """
        for item in range(minimum_num, maximum_num+1):
            str_item = str(item)
            if len(str_item) < 6:
                str_item = '0' * (6 - len(str_item)) + str_item
            self.__tickets.append(Ticket(str_item))

    def count_happy_tickets(self, is_all=False):
        """
        Go through list __tickets and call method with particular algorithm
        of check is ticket happy, count and print happy tickets and algorithm
        :return:
        """
        if is_all:
            self.count_lucky_ticket(6)
        else:
            self.__count = 0
            if self.__tickets:
                for ticket in self.__tickets:
                    is_happy = ticket.is_happy(self.__algorithm)
                    if is_happy:
                        self.__count += 1

    def print_counting_result(self):
        print("Number of happy tickets by {0} method is equal - {1}".format(self.__algorithm, self.__count))

    def tickets_input(self):
        def tickets_input():
            """
            Control input tickets and output instructions for user
            for test 2 -from file mode use - 'data/tickets.txt' - file with tickets
            """
        flag = True
        while flag:
            print(
                  "Choose type of tickets input:\n"
                  " [1] manual tickets input,\n"
                  " [2] load tickets from file,\n"
                  " [3] generate tickets between min and max values,\n"
                  " [4] calculate maximum number of happy tickets,\n"
                 )
            input_type = input()
            if input_type == '1':
                self.input_tickets_manually()
                self.count_happy_tickets()
                flag = False
            elif input_type == '2':
                self.get_tickets_from_file()
                self.count_happy_tickets()
                flag = False
            elif input_type == '3':
                self.get_tickets_from_numbers()
                self.count_happy_tickets()
                flag = False
            elif input_type == '4':
                self.count_happy_tickets(True)
                flag = False
            else:
                print("Your choose not correct please type 1 or 2 or 3 or 4")
                flag = __class__.do_continue()
        return self.tickets != []

    def __number_count(self, i_number):
        """
        Calculate table of sum of left digits and number of tickets with this sum
        for tickets with i_number digits
        :param i_number:
        :return:
        """
        i_half = int(i_number / 2)
        a_data = {}
        for i in range(1, i_half + 1):
            i_len = i * 9 + 1
            if i == 1:
                for j in range(i_len):
                    if j == 0:
                        a_data[i] = {0: 1}
                    else:
                        a_data[i][j] = 1
            else:
                i_sum = 0
                k = 0
                a_data[i] = {}
                while k <= i_len / 2:
                    i_sum += a_data[i - 1][k]
                    if k >= 10:
                        i_sum -= a_data[i - 1][k - 10]
                    a_data[i][k] = i_sum
                    k += 1
                while k < i_len:
                    a_data[i][k] = a_data[i][i_len - 1 - k]
                    k += 1
        return a_data

    def count_lucky_ticket(self, i_number):
        """
        Count all lucky tickets fon i_number digits in ticket
        :param i_number:
        :return:
        """
        i_half = int(i_number / 2)
        a_data = self.__number_count(i_number)
        i_count = 0
        for i in range(i_half * 9 + 1):
            i_count += a_data[i_half][i] ** 2
        self.__count = i_count

    @property
    def tickets(self):
        return self.__tickets

    @property
    def count(self):
        return self.__count

    @property
    def algorithm(self):
        return self.__algorithm

    @staticmethod
    def start():
        """
        Start application function
        :return:
        """
        handler = TicketHandler()
        if handler.input_mark():
            if handler.tickets_input():
                handler.print_counting_result()


if __name__ == "__main__":
    TicketHandler.start()
