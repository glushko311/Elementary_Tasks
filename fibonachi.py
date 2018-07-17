
from optparse import OptionParser

from task_validator import TaskValidator


class Fibonachi:
    """
    Contain methods to work with fibonachi sequence
    """

    @classmethod
    def fib_in_interval(cls, min_val: int, max_val: int) -> list:
        """
        Return sequence of fibonachi numders between min and max
        :param min_val:
        :param max_val:
        :return:
        """
        fib = [0, 1]
        while fib[-1] < max_val:
            if fib[-1] < min_val:
                fib.append(fib[-2] + fib[-1])
                fib.pop(0)
            else:
                fib.append(fib[-2] + fib[-1])
        fib.pop(0)
        if fib[-1] != max_val:
            fib.pop(-1)
        if not min_val:
            fib.insert(0, 0)
        return fib

    @classmethod
    def print_arr(cls, fib_arr: list):
        """
        Print list of fibonachi numbers
        :param fib_arr:
        :return:
        """
        fib_arr = map(lambda x: str(x), fib_arr)
        print(', '.join(fib_arr))


def start():
    """
    Start application function
    :return:
    """

    parser = OptionParser()
    args = parser.parse_args()

    validation_res = TaskValidator.validate_fibonachi(args)
    if validation_res[0]:
        fib_arr = Fibonachi.fib_in_interval(int(args[1][0]), int(args[1][1]))
        Fibonachi.print_arr(fib_arr)
    else:
        print(validation_res[1])


if __name__ == "__main__":
    start()
