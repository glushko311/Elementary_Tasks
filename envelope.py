from math import sin, cos, pi


class Envelope:
    '''
    Contain envelope data and methods
    parameters:
    __max_side
    __min_side
    __square
    Methods
    is_into(env1, env2) - calculate can you put one envelope to another
    get_n_validate() - get data from user validate and transmit them
                       to constructor
    max_side() - getter for __max_side
    min_side() - getter for __min_side
    square() - getter for __square
    '''

    @staticmethod
    def is_into(env1, env2):
        '''
        Calculate can you put one envelope to another
        :param env1:
        :param env2:
        :return: (Envelope, Envelope, bool)
        '''
        is_in_flag = False
        if env1.square < env2.square:
            env1, env2 = env2, env1

        if env1.max_side > env2.max_side and env1.min_side > env2.min_side:
            is_in_flag = True
        else:
            phi = 0  # rotation angle for envelope2
            accuracy = 0.001  # angle step
            # Check - can put envelope2 into envelope1 if it is rotate to angle phi
            while phi < (pi / 2):
                if (env1.max_side >= (env2.max_side * sin(phi) + env2.min_side * cos(phi))) and\
                        (env1.min_side >= env2.max_side * cos(phi) + env2.min_side * sin(phi)):
                    is_in_flag = True
                phi += accuracy
        return env2, env1, is_in_flag

    @staticmethod
    def get_n_validate():
        '''
        get data from user validate and transmit them
        :return:Envelope
        '''
        a_side = input("Input envelope height - ")
        a_side = float(a_side)
        if a_side <= 0:
            raise ValueError
        b_side = input("Input envelope length - ")
        b_side = float(b_side)
        if b_side <= 0:
            raise ValueError

        return Envelope(a_side, b_side)

    def __init__(self, a_side: float, b_side: float):
        self.__max_side = max(a_side, b_side)
        self.__min_side = min(a_side, b_side)
        self.__square = a_side * b_side

    @property
    def max_side(self):
        return self.__max_side

    @property
    def min_side(self):
        return self.__min_side

    @property
    def square(self):
        return self.__square

    def __repr__(self):
        return "envelope with sides {0} and {1}".format(self.max_side, self.min_side,)

    def __eq__(self, other):
        if self.min_side == other.min_side and self.max_side == other.max_side:
            return True
        else:
            return False


def input_envelope(name):
    while 1:
        try:
            env = Envelope.get_n_validate()
            return env
        except ValueError:
            print("Invalid data input for {0} envelope. Sides should be positive numbers".format(name))
            continue


def start():
    flag = True
    while flag:
        env1 = input_envelope("first")
        env2 = input_envelope("second")

        res = Envelope.is_into(env1, env2)
        if res[2]:
            print("You can put {0} into {1}".format(res[0], res[1]))
        else:
            print("You can't put envelopes one to another")

        want_continue = (input("Would you like to continue? \'y\', \'Yes\' / \'n\', \'No\'")).upper()
        if not (want_continue == 'Y' or want_continue == 'YES'):
            flag = False


if __name__ == "__main__":
    start()
