from math import sin, cos, pi

from exceptions.envelope_error import EnvelopeError
from validator import Validator


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
    def can_put_one_to_another_or_opposite(env1, env2):
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


def input_envelope():
    flag = True
    while flag:
        print("Please input the first side")
        print("To stop input and quit press q or Q")
        a_side = input()
        flag = not a_side.lower() == "q"
        if not flag:
            continue
        validation_res = Validator.validate_positive_not_null(a_side)
        if not validation_res[0]:
            print(validation_res[1])
            continue
        print("Please input the second side")
        b_side = input()
        flag = not b_side.lower().lower() == "q"
        if not flag:
            continue
        validation_res = Validator.validate_positive_not_null(b_side)
        if not validation_res[0]:
            print(validation_res[1])
            continue
        return Envelope(float(a_side), float(b_side))
    raise EnvelopeError("User exit")


def start():
    flag = True
    while flag:
        try:
            print("Please input first envelope sides")
            env1 = input_envelope()
        except EnvelopeError as e:
            print(e)
            quit()
        try:
            print("Please input second envelope sides")
            env2 = input_envelope()
        except EnvelopeError as e:
            print(e)
            quit()
        res = Envelope.can_put_one_to_another_or_opposite(env1, env2)
        if res[2]:
            print("You can put {0} into {1}".format(res[0], res[1]))
        else:
            print("You can't put envelopes one to another")

        want_continue = (input("Would you like to continue? \'y\', \'Yes\'")).upper()
        if not (want_continue.lower() in ('y', 'yes')):
            flag = False


if __name__ == "__main__":
    start()
