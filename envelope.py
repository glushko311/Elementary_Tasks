from math import sin, cos, pi, asin, acos

from exceptions.user_exit_error import UserExitError

from task_validator import TaskValidator


class Envelope:
    """
    Contain envelope data and methods
    parameters:
    __max_side
    __min_side
    __square
    Methods
    can_put_other(other) - calculate can you put other Envelope into self
    calc_rotation_angle_for_other(other) - calculate best rotation angle for
                    other Envelope in self
    max_side() - getter for __max_side
    min_side() - getter for __min_side
    square() - getter for __square
    """

    # @staticmethod
    # def can_put_one_to_another_or_opposite(env1, env2):
    #     '''
    #     Calculate can you put one envelope to another
    #     :param env1:
    #     :param env2:
    #     :return: (Envelope, Envelope, bool)
    #     '''
    #     is_in_flag = False
    #     if env1.square < env2.square:
    #         env1, env2 = env2, env1
    #
    #     if env1.max_side > env2.max_side and env1.min_side > env2.min_side:
    #         is_in_flag = True
    #     else:
    #         phi = 0  # rotation angle for envelope2
    #         accuracy = 0.001  # angle step
    #         # Check - can put envelope2 into envelope1 if it is rotate to angle phi
    #         while phi < (pi / 2):
    #             if (env1.max_side >= (env2.max_side * sin(phi) + env2.min_side * cos(phi))) and\
    #                     (env1.min_side >= env2.max_side * cos(phi) + env2.min_side * sin(phi)):
    #                 is_in_flag = True
    #             phi += accuracy
    #     return env2, env1, is_in_flag

    def calc_rotation_angle_for_other(self, other):
        """
        Calculate the best rotation angle for other into self
        :param other:
        :return:
        """
        j = asin(other.max_side / ((other.max_side ** 2 + other.min_side ** 2) ** 0.5))

        phi = j - acos(self.min_side / ((other.max_side ** 2 + other.min_side ** 2) ** 0.5)) + 2 * pi

        return phi

    def can_put_other(self, other):
        """
        Check can you put other Envelope into self
        :param other: Envelope
        :return:
        """
        if self.square < other.square:
            return False
        if self.max_side > other.max_side and self.min_side > other.min_side:
            return True
        else:
            rotate_angle = self.calc_rotation_angle_for_other(other)
            projection_on_max_side = other.max_side * cos(rotate_angle) + other.min_side * sin(rotate_angle)
            if projection_on_max_side < self.max_side:
                return True
            else:
                return False

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
        return "envelope with sides {0} and {1}".format(self.max_side, self.min_side, )

    def __eq__(self, other):
        if self.min_side == other.min_side and self.max_side == other.max_side:
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


def input_envelope():
    """
    Input data for create one envelope send data into validator
    :return: Envelope|raise UserExitError
    """
    flag = True
    while flag:
        print("Please input the first side")
        a_side = input()
        print("Please input the second side")
        b_side = input()
        validation_res = TaskValidator.validate_envelope_sides(a_side, b_side)
        if validation_res[0]:
            return Envelope(float(a_side), float(b_side))
        print(validation_res[1])
        flag = do_continue()

    raise UserExitError("User exit")


def start():
    flag = True
    while flag:
        try:
            print("Please input first envelope sides")
            env1 = input_envelope()
            print("Please input second envelope sides")
            env2 = input_envelope()
        except UserExitError as e:
            print(e)
            flag = False
            continue
        if env2.square > env1.square:
            env1, env2 = env2, env1
        res = env1.can_put_other(env2)
        if res:
            print("You can put {0} into {1}".format(env2, env1))
        else:
            print("You can't put envelopes one to another")
        flag = do_continue()


if __name__ == "__main__":
    start()
