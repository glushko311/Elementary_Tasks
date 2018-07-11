import unittest
import os

from file_handler import FileHandler


class FileHandlerTestSuit(unittest.TestCase):
    def test_file_n_count_valid(self):
        with open("parser_auto_test.txt", "w") as f:
            f.write("abra kadabra\n abra kadabra")
        res = FileHandler.find_n_count("parser_auto_test.txt", "kad")
        os.remove("parser_auto_test.txt")
        self.assertEqual(res, 2)

    def test_file_n_count_none(self):
        with open("parser_auto_test.txt", "w") as f:
            f.write("abra kadabra\n abra kadabra")
        res = FileHandler.find_n_count("parser_auto_test.txt", "kasa")
        os.remove("parser_auto_test.txt")
        self.assertEqual(res, 0)

    def test_file_n_count_not_found(self):
        with self.assertRaises(FileNotFoundError):
            FileHandler.find_n_count("not_found.txt", "kad")

    def test_find_n_replace_valid(self):
        with open("parser_auto_test.txt", "w") as f:
            f.write("abra kadabra\n abra kadabra")
        res = FileHandler.find_n_replace("parser_auto_test.txt", "kad", "m")
        with open("parser_auto_test.txt", "r") as f:
            act_res = f.read()
            exp_res = "abra mabra\n abra mabra"
        os.remove("parser_auto_test.txt")
        self.assertEqual(act_res, exp_res)

    def test_find_n_replace_not_found(self):
        with self.assertRaises(FileNotFoundError):
            FileHandler.find_n_replace("not_found.txt", "kad", "mab")

if __name__ == '__main__':
        unittest.main()