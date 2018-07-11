from triangular_exception import TriangularException
class Triangular:
    '''
    Contain triangular parameters and methods
    Parameters:
        side_a, side_b, side_c - length of sides of triangle
        name - name of triangle
        square - square of triangle
    Methods:
          get_n_validate() - get data from user and if they
                            valid return Triangular object
          sort_triangular_list(triangular_list) - Sort triangular
                            list by square field and return sorted
    '''

    @staticmethod
    def get_n_validate():
        '''
        get data from user and if they valid return Triangular object
        :return: Triangular
        '''
        input_data = input().split(',')
        name = (input_data[0]).strip()
        if not len(name):
            raise TriangularException('Blank name not available!')
        side_a = float(input_data[1])
        side_b = float(input_data[2])
        side_c = float(input_data[3])
        p = 0.0
        p = (side_a + side_b + side_c)/2
        if (p-side_a) * (p-side_b) * (p-side_c) <= 0:
            raise TriangularException('It is impossible to create this triangle '
                             'one of sides too long')
        square = (p * (p-side_a) * (p-side_b) * (p-side_c)) ** 0.5
        return Triangular(side_a, side_b, side_c, square, name)

    @staticmethod
    def sort_triangular_list(triangle_list: list):
        '''
        Sort triangular list by square field and return sorted
        :param triangle_list:
        :return triangle_list:
        '''
        return sorted(triangle_list, key=lambda x: x.square, reverse=True)

    def __init__(self, side_a, side_b, side_c, square, name):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        self.__name = name
        self.__square = square

    def __str__(self):
        return "1.[{0}]: {1} sm".format(self.__name, round(self.__square, 2))

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

def start():
    '''
    Start application function
    get and process data from user and put them into list
    compare and sort triangulars by square
    print triangulars
    :return None:
    '''
    triangular_list = []
    is_continue_flag = True
    while is_continue_flag:
        input_triang_flag = True
        while input_triang_flag:
            try:
                print("Input triangle data. Input format - \"name,side_a,side_b,side_c\".")
                triangular_list.append(Triangular.get_n_validate())
            except ValueError:
                print("Not valid data input format. Try again.")
                continue
            except IndexError:
                print("Not valid data input format. Try again.")
                continue
            except TriangularException as e:
                print(str(e))
            input_triang_flag = False
        want_continue = (input("Хотите ли вы продолжить \'y\' или \'Yes\'")).upper()
        if not (want_continue == 'Y' or want_continue == 'YES'):
            is_continue_flag = False

    triangular_list = Triangular.sort_triangular_list(triangular_list)

    print("============= Triangular List: =============")
    for triangular in triangular_list:
        print(triangular)


if __name__ == "__main__":
    start()
