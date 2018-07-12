from optparse import OptionParser

from exceptions.chess_board_exception import ChessBoardException


class ChessBoard:
    '''
    Class ChessBoard
        Object of class contain data of a chess board and have methods to display it
        Parameters:
         __board_odd_row - list of boolean
         __board_even_row - list of boolean
         __length - integer
         __height - integer

         Methods:
             __init__(height, length)
             print_board()
             show_instructions()
    '''
    '''
    Validate single value - return true or Exception
    '''
    @staticmethod
    def validate_value(value, name=""):
        if value is None:
            raise ChessBoardException('{0} value  not exists'.format(name))
        if not value.isdigit():
            raise ChessBoardException('{0} value not a number'.format(name))
        value = int(value)
        if value <= 0:
            raise ChessBoardException('{0} value should be more than null'.format(name))
        return True

    '''
    Validate list of arguments - return ChessBoard object or Exception
    '''
    @staticmethod
    def get_n_validate(args):
        if len(args) != 2:
            raise ChessBoardException('Should be started with two parameters')
        length = args[0]
        height = args[1]

        ChessBoard.validate_value(length, 'Length')
        ChessBoard.validate_value(height, 'Height')

        return ChessBoard(int(length), int(height))

    '''
        Method used to display instructions to input parameters
    '''
    @staticmethod
    def show_instructions():
        '''
        Display text documentation how to use application
        :return None:
        '''
        print(
            '''
            Please start application with two parameters,
            parameters should be positive numbers
            for example:
            $ python main.py 5 6
            '''
        )

    def __init__(self, height, length):
        self.__length = length
        self.__height = height
        self.__board_odd_row = []
        self.__board_even_row = []
        for i in range(length):
            if i % 2:
                self.__board_even_row.append(True)
            else:
                self.__board_even_row.append(False)

        if length % 2:
            self.__board_odd_row = list(map(lambda x: not x, self.__board_even_row))
        else:
            self.__board_odd_row = self.__board_even_row[::-1]


    '''
        Method used to display chess board with symbols " " and "*"
    '''
    def print_board(self):
        board = []
        for i in range(self.__height):
            if i % 2:
                board.append(self.__board_even_row)
            else:
                board.append(self.__board_odd_row)
        for i in board:
            for j in i:
                if j:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    @property
    def length(self):
        return self.__length

    @property
    def height(self):
        return self.__height

    def __eq__(self, other):
        if self.length == other.length and self.height == other.height:
            return True
        else:
            return False


def start():
    parser = OptionParser()
    args = parser.parse_args()

    try:
        board = ChessBoard.get_n_validate(args[1])
    except ChessBoardException as e:
        print(e)
        ChessBoard.show_instructions()
        quit()

    board.print_board()

if __name__ == "__main__":
    start()