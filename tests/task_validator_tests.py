import unittest

from nose_parameterized import parameterized

from task_validator import TaskValidator


class TaskValidatorTestList(unittest.TestCase):

    @parameterized.expand([
        [
            "test_validate_chess_board_list, value valid numbers",
            [[], ['12', '7']], (True, 'Validation successful')
        ],
        [
            "test_validate_chess_board_list, first value strings",
            [[], ['a', '7']], (False, 'First argument - height is invalid\nValue is not an integer number.\n')
        ],
        [
            "test_validate_chess_board_list, second value strings",
            [[], ['5', 'a']], (False, 'Second argument - length is invalid\nValue is not an integer number.\n')
        ],
        [
            "test_validate_chess_board_list, second value float",
            [[], ['5', '5.87']], (False, 'Second argument - length is invalid\nValue is not an integer number.\n')
        ],
        [
            "test_validate_chess_board_list, value negative",
            [[], ['-4', '7']], (False, 'First argument - height is invalid\nValue is negative.\n')
        ],
    ])
    def test_validate_chess_board_list(self, name, value, exp_res):
        act_res = (TaskValidator.validate_chess_board_list(value))
        try:
            self.assertEqual(act_res[0], exp_res[0])
            self.assertEqual(act_res[1], exp_res[1])
        except AssertionError as e:
            msg = "\nFail test - \"{0}\"; Input data - {1}; Error{2}".format(name, value, e)
            raise AssertionError(msg)

    @parameterized.expand([
        [
            "validate_envelope_sides, values integer",
            "12",
            "23",
            (True, 'Validation successful')
        ],
        [
            "validate_envelope_sides, values float",
            "12.45",
            "23.76",
            (True, 'Validation successful')
        ],
        [
            "validate_envelope_sides, first value negative",
            '-4',
            '7',
            (False, 'First argument - height is invalid\nValue is negative.\n')
        ],
        [
            "validate_envelope_sides, second value negative",
            '4',
            '-7',
            (False, 'Second argument - length is invalid\nValue is negative.\n')
        ],
    ])
    def test_validate_envelope_sides(self, name, side_a, side_b, exp_res):
        act_res = (TaskValidator.validate_envelope_sides(side_a, side_b))
        try:
            self.assertEqual(act_res[0], exp_res[0])
            self.assertEqual(act_res[1], exp_res[1])
        except AssertionError as e:
            msg = "\nFail test - \"{0}\"; Input data - {1}; Error{2}".format(name, (side_a, side_b), e)
            raise AssertionError(msg)

    @parameterized.expand([
        [
            "validate_triangular, valid values float and integer",
            "some_name,12,11.33,13",
            (True, 'Validation successfully')
        ],
        [
            "validate_triangular, empty input",
            "",
            (False, "Invalid value, value format should be \"name,side_a,side_b,side_c\".")
        ],
        [
            "validate_triangular, not number side",
            "some_name,12,aaa,13",
            (False, "Side validation error.\nValue is not a float number.\n")
        ],
        [
            "validate_triangular, one side is too large",
            "some_name,12,66,13",
            (False, "It is impossible to create this triangle one of sides too long")
        ],
        [
            "validate_triangular, null side",
            "ttt,12,0,13",
            (False, "Side validation error.\nValue is null.\n")
        ],
        [
            "validate_triangular, negative side",
            "ttt,-12,-11,-13",
            (False, "Side validation error.\nValue is negative.\n")
        ],
    ])
    def test_validate_triangular(self, name, triang_str, exp_res):
        act_res = (TaskValidator.validate_triangular(triang_str))
        try:
            self.assertEqual(act_res[0], exp_res[0])
            self.assertEqual(act_res[1], exp_res[1])
        except AssertionError as e:
            msg = "\nFail test - \"{0}\"; Input data - {1}; Error{2}".format(name, triang_str, e)
            raise AssertionError(msg)

    @parameterized.expand([
        [
            "test_validate_file_handler, valid list with exists file",
            [[], ["task_validator_tests.py"]],
            (True, 'Validation successful')
        ],
        [
            "test_validate_file_handler, valid list non exists file",
            [[], ["tttt.py"]],
            (False, "File with path tttt.py not found!")
        ],
        [
            "test_validate_file_handler, empty args list",
            [[], []],
            (False, "Application should be started with two or three parameters:\n "
                    "1 - path to file, 2 - substring to find [, 3 - substring to replace]")
        ],
    ])
    def test_validate_file_handler(self, name, arg_list, exp_res):
        act_res = TaskValidator.validate_file_handler(arg_list)
        try:
            self.assertEqual(act_res[0], exp_res[0])
            self.assertEqual(act_res[1], exp_res[1])
        except AssertionError as e:
            msg = "\nFail test - \"{0}\"; Input data - {1}; Error{2}".format(name, arg_list, e)
            raise AssertionError(msg)

    @parameterized.expand([
        [
            "test_validate_number_translation, valid number",
            [[], ["12", ]],
            (True, 'Validation successful')
        ],
        [
            "test_validate_number_translation, valid large",
            [[], [str(10 ** 101)]],
            (True, 'Validation successful')
        ],
        [
            "test_validate_number_translation, valid negative",
            [[], ["-12", ]],
            (True, 'Validation successful')
        ],
        [
            "test_validate_number_translation, valid null",
            [[], ["0", ]],
            (True, 'Validation successful')
        ],
        [
            "test_validate_number_translation, empty",
            [[], []],
            (False, 'Start application with one number parameter!')
        ],
        [
            "test_validate_number_translation, float",
            [[], ["12.33"]],
            (False, 'Value is not an integer number.\n')
        ],
        [
            "test_validate_number_translation, not valid large",
            [[], [str(10 ** 103)]],
            (False, 'Your input number is too large, it should be less then 10 ** 102 - 1')
        ],

        # [
        #     "test_validate_number_translation, empty args list",
        #     [[], []],
        #     (False, "Application should be started with two or three parameters:\n "
        #             "1 - path to file, 2 - substring to find [, 3 - substring to replace]")
        # ],
    ])
    def test_validate_number_translation(self, name, data_list, exp_res):
        act_res = TaskValidator.validate_number_translation(data_list)
        try:
            self.assertEqual(act_res[0], exp_res[0])
            self.assertEqual(act_res[1], exp_res[1])
        except AssertionError as e:
            msg = "\nFail test - \"{0}\"; Input data - {1}; Error{2}".format(name, data_list, e)
            raise AssertionError(msg)

    @parameterized.expand([
        [
            "test_validate_fibonachi, value valid numbers",
            [[], ['12', '23']], (True,)
        ],
        [
            "test_validate_fibonachi, first null",
            [[], ['0', '23']], (True,)
        ],
        [
            "test_validate_fibonachi, first value strings",
            [[], ['a', '7']], (False,)
        ],
        [
            "test_validate_fibonachi, second value strings",
            [[], ['5', 'a']], (False,)
        ],
        [
            "test_validate_fibonachi, second value float",
            [[], ['2', '8.87']], (False,)
        ],
        [
            "test_validate_fibonachi, value negative",
            [[], ['-4', '7']], (False,)
        ],
        [
            "test_validate_fibonachi, first larger then second",
            [[], ['22', '7']], (False,)
        ],
    ])
    def test_validate_fibonachi(self, name, data_list, exp_res):
        act_res = (TaskValidator.validate_fibonachi(data_list))
        try:
            self.assertEqual(act_res[0], exp_res[0])
        except AssertionError as e:
            msg = "\nFail test - \"{0}\"; Input data - {1}; Error{2}".format(name, data_list, e)
            raise AssertionError(msg)

    @parameterized.expand([
        [
            "test_validate_sequence, value valid number",
            [[], ['23']], (True,)
        ],
        [
            "test_validate_sequence, value null",
            [[], ['0', ]], (True,)
        ],
        [
            "test_validate_sequence, value null",
            [[], ['a', ]], (False,)
        ],
        [
            "test_validate_sequence, value negative",
            [[], ['-4', ]], (False,)
        ],
        [
            "test_validate_sequence, empty",
            [[], []], (False,)
        ],
    ])
    def test_validate_sequence(self, name, data_list, exp_res):
        act_res = (TaskValidator.validate_sequence(data_list))
        try:
            self.assertEqual(act_res[0], exp_res[0])
        except AssertionError as e:
            msg = "\nFail test - \"{0}\"; Input data - {1}; Error{2}".format(name, data_list, e)
            raise AssertionError(msg)


if __name__ == '__main__':
    unittest.main()
