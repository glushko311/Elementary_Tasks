import unittest
from optparse import OptionParser


class Fibonachi:
    '''
    Contain methods to work with fibonachi sequence
    '''

    @classmethod
    def fib_in_interval(cls, min: int, max: int) -> list:
        '''
        Return sequence of fibonachi numders between min and max
        :param min:
        :param max:
        :return:
        '''
        fib = [0, 1]
        while fib[-1] < max:
            if fib[-1] < min:
                fib.append(fib[-2] + fib[-1])
                fib.pop(0)
            else:
                fib.append(fib[-2] + fib[-1])
        fib.pop(0)
        if fib[-1] != max:
            fib.pop(-1)
        if not min:
            fib.insert(0, 0)
        return fib

    @classmethod
    def print_arr(cls, fib_arr: list) -> str:
        '''
        Print list of fibonachi numbers
        :param fib_arr:
        :return:
        '''
        fib_arr = map(lambda x: str(x), fib_arr)
        print(', '.join(fib_arr))


def start():
    '''
    Start application function
    :return:
    '''
    parser = OptionParser()
    args = parser.parse_args()

    try:
        min_val = int(args[1][0])
        max_val = int(args[1][1])
        if min_val < 0 or max_val < 0 or min_val > max_val:
            raise TypeError
    except IndexError:
        print("Start application with two number parameters!")
        quit()
    except ValueError:
        print("Parameters should be numeric!")
        quit()
    except TypeError:
        print("Second parameter should be larger than first!")
        print("Parameters should be larger than 0!")
        quit()

    fib_arr = Fibonachi.fib_in_interval(min_val, max_val)
    Fibonachi.print_arr(fib_arr)


if __name__ == "__main__":
    start()
