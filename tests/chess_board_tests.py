import unittest

from chess_board import ChessBoard
from chess_board_exception import ChessBoardException


class ChessBoardTestSuit(unittest.TestCase):
    # for validate_value method
    def test_validate_valid(self):
        res = ChessBoard.validate_value('4', "bbb")
        self.assertEqual(res, True)

    def test_validate_valid2(self):
        res = ChessBoard.validate_value('8')
        self.assertEqual(res, True)

    def test_validate_null(self):
        with self.assertRaises(ChessBoardException):
            ChessBoard.validate_value('0', "aaa")

    def test_validate_negative(self):
        with self.assertRaises(ChessBoardException):
            ChessBoard.validate_value('-5', "aaa")

    def test_validate_string(self):
        with self.assertRaises(ChessBoardException):
            ChessBoard.validate_value('aaa', "aaa")

    def test_validate_float(self):
        with self.assertRaises(ChessBoardException):
            ChessBoard.validate_value('4.2', "aaa")

    # for get_n_validate method
    def test_get_n_validate_valid(self):
        res = ChessBoard.get_n_validate(('4', '4'))
        self.assertEqual(res, ChessBoard(4, 4))

    def test_get_n_validate_one(self):
        with self.assertRaises(ChessBoardException):
            ChessBoard.get_n_validate(['4'])

    def test_get_n_validate_str(self):
        with self.assertRaises(ChessBoardException):
            ChessBoard.get_n_validate(['a', '4'])

    def test_get_n_validate_null(self):
        with self.assertRaises(ChessBoardException):
            ChessBoard.get_n_validate(['0', '0'])

    def test_get_n_validate_negative(self):
        with self.assertRaises(ChessBoardException):
            ChessBoard.get_n_validate(['4', '-4'])

    def test_get_n_validate_float(self):
        with self.assertRaises(ChessBoardException):
            ChessBoard.get_n_validate(['4.5', '4.3'])

if __name__ == '__main__':
        unittest.main()
