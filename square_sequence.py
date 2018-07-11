from optparse import OptionParser


class Sequence:

    @staticmethod
    def get_n_validate(args):
        num = int(args[1][0])
        if num < 0:
            raise ValueError
        return Sequence([str(i) for i in range(1, num**2) if i**2 < num])

    def __init__(self, sequence):
        self.sequence = sequence

    def __str__(self):
        return ", ".join(self.sequence)

    @staticmethod
    def start():
        '''
        Start application function
        :return:
        '''
        parser = OptionParser()
        args = parser.parse_args()
        try:
            sequence = Sequence.get_n_validate(args)
        except IndexError:
            print("Start application with single number parameter")
            quit()

        except ValueError:
            print("Start application with single number parameter")
            quit()

        print(sequence)


if __name__ == "__main__":
    Sequence.start()

