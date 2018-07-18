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
            "12", "23", (True, 'Validation successful')
         ],
        [
            "validate_envelope_sides, values float",
            "12.45", "23.76", (True, 'Validation successful')
         ],
        [
            "validate_envelope_sides, first value negative",
            '-4', '7', (False, 'First argument - height is invalid\nValue is negative.\n')
         ],
        [
            "validate_envelope_sides, second value negative",
            '4', '-7', (False, 'Second argument - length is invalid\nValue is negative.\n')
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
            "some_name,12,11.33,13", (True, 'Validation successfully')
         ],
        [
            "validate_triangular, empty input",
            "", (False, "Invalid value, value format should be \"name,side_a,side_b,side_c\".")
         ],
        [
            "validate_triangular, not number side",
             "some_name,12,aaa,13", (False, "Side validation error.\nValue is not a float number.\n")
         ],
        [
            "validate_triangular, one side is too large",
             "some_name,12,66,13", (False, "It is impossible to create this triangle one of sides too long")
         ],
        [
            "validate_triangular, null side",
             "ttt,12,0,13", (False, "Side validation error.\nValue is null.\n")
         ],
        [
            "validate_triangular, negative side",
             "ttt,-12,-11,-13", (False, "Side validation error.\nValue is negative.\n")
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


if __name__ == '__main__':
    unittest.main()
