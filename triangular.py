
from task_validator import TaskValidator
# from exceptions.triangular_exception import TriangularException


class Triangular:
    """
    Contain triangular parameters and methods
    Parameters:
        side_a, side_b, side_c - length of sides of triangle
        name - name of triangle
        square - square of triangle
    Methods:
          sort_triangular_list(triangular_list) - Sort triangular
                            list by square field and return sorted
    """
    @staticmethod
    def triangular_create(triang_str:str):
        triang_list = triang_str.split(',')
        name = triang_list[0].strip()
        side_a = float(triang_list[1].strip())
        side_b = float(triang_list[2].strip())
        side_c = float(triang_list[3].strip())
        p = (side_a + side_b + side_c) / 2
        square = (p * (p - side_a) * (p - side_b) * (p - side_c)) ** 0.5
        return Triangular(side_a, side_b, side_c, square, name)

    @staticmethod
    def sort_triangular_list(triangle_list: list):
        """
        Sort triangular list by square field and return sorted
        :param triangle_list:
        :return triangle_list:
        """
        return sorted(triangle_list, key=lambda x: x.square, reverse=True)

    def __init__(self, side_a, side_b, side_c, square, name):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        self.__name = name
        self.__square = square

    def __str__(self):
        return "1.[{0}]: {1} sm2".format(self.__name, round(self.__square, 2))

    @property
    def square(self):
        return self.__square

    @property
    def side_a(self):
        return self.__side_a

    @property
    def side_b(self):
        return self.__side_b

    @property
    def side_c(self):
        return self.__side_c

    @property
    def name(self):
        return self.__name

    def __eq__(self, other):
        this_set = {self.side_a, self.side_b, self.side_c}
        other_set = {other.side_a, other.side_b, other.side_c}
        if this_set.difference(other_set) == set() and \
                self.name == other.name:
            return True
        else:
            return False


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


def start():
    """
    Start application function
    get and process data from user and put them into list
    compare and sort triangulars by square
    print triangulars
    :return: None
    """

    triangular_list = []
    input_triang_flag = True
    while input_triang_flag:
        print("Input triangle data. Input format - \"name,side_a,side_b,side_c\".")
        input_data = input()
        validate_res = TaskValidator.validate_triangular(input_data)
        if validate_res[0]:
            triangular_list.append(Triangular.triangular_create(input_data))
            input_triang_flag = do_continue()
        else:
            print(validate_res[1])
            input_triang_flag = do_continue()

    triangular_list = Triangular.sort_triangular_list(triangular_list)
    print("============= Triangular List: =============")
    for triangular in triangular_list:
        print(triangular)


if __name__ == "__main__":
    start()
