from optparse import OptionParser

from exceptions.chess_board_exception import ChessBoardException
from validator import Validator


class ChessBoard:
    """
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
    """

    @staticmethod
    def create_chessboard(args):
        """
        Send list of arguments to validator if ok - create ChessBoard object else ChessBoardException
        """
        if len(args) != 2:
            raise ChessBoardException('Should be started with two parameters')
        length = args[0]
        height = args[1]
        validation_res = Validator.validate_two_int_not_null(length, height)
        if validation_res[0]:
            return ChessBoard(int(length), int(height))
        else:
            raise ChessBoardException(validation_res[1])

    @staticmethod
    def show_instructions():
        """
            Display text documentation how to use application
            :return None:
        """
        print(
            """
                Please start application with two parameters,
                parameters should be positive numbers
                for example:
                $ python chess_board.py 5 6
            """
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

    def print_board(self):
        """
            Method used to display chess board with symbols " " and "*"
        """
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
    """
        Start application function
    :return:
    """
    parser = OptionParser()
    args = parser.parse_args()

    try:
        board = ChessBoard.create_chessboard(args[1])
        board.print_board()
    except ChessBoardException as e:
        print(e)
        ChessBoard.show_instructions()


if __name__ == "__main__":
    start()
