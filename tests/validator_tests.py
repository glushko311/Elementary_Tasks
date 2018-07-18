import unittest

from nose_parameterized import parameterized

from validator import Validator


class ValidatorTestList(unittest.TestCase):

    @parameterized.expand([
        ["test_validate_is_null, value valid number - 12", "12", (True, 'Validation successfully.\n')],
        ["test_validate_is_null, value null - 0", "0", (False, 'Value is null.\n')],
        ["test_validate_is_null, value null - 0000", "0000", (False, 'Value is null.\n')],

    ])
    def test_validate_is_null(self, name, value, exp_res):
        act_res = (Validator.validate_is_not_null(value))
        try:
            self.assertEqual(act_res[0], exp_res[0])
            self.assertEqual(act_res[1], exp_res[1])
        except AssertionError as e:
            msg = "\nFail test - \"{0}\"; Input data - {1}; Error{2}".format(name, value, e)
            raise AssertionError(msg)

    @parameterized.expand([
        ["test_validate_is_not_negative, value - positive number", "12", (True, 'Validation successfully.\n')],
        ["test_validate_is_not_negative, value - null", "0", (True, 'Validation successfully.\n')],
        ["test_validate_is_not_negative, value - negative number", '-123', (False, "Value is negative.\n")],
        ["test_validate_is_not_negative, value - negative float", "-12.1", (False, "Value is negative.\n")],
        ["test_validate_is_not_negative, value - positive number with +", "+12.1", (True, 'Validation successfully.\n')]
    ])
    def test_validate_is_not_negative(self, name, value, exp_res):
        act_res = (Validator.validate_is_not_negative(value))
        try:
            self.assertEqual(act_res[0], exp_res[0])
            self.assertEqual(act_res[1], exp_res[1])
        except AssertionError as e:
            msg = "\nFail test - \"{0}\"; Input data - {1}; Error{2}".format(name, value, e)
            raise AssertionError(msg)

    @parameterized.expand([
        ["test_validate_is_int, value - positive number", "12", (True, "Validation successfully.\n")],
        ["test_validate_is_int, value - negative number", "-12", (True, "Validation successfully.\n")],
        ["test_validate_is_int, value - negative number", "-12", (True, "Validation successfully.\n")],
        ["test_validate_is_int, value - null", "0", (True, "Validation successfully.\n")],
        ["test_validate_is_int, value - string", "aa", (False, "Value is not an integer number.\n")],
        ["test_validate_is_int, value - number and string", "5a", (False, "Value is not an integer number.\n")],
        ["test_validate_is_int, value - float number", "5.232", (False, "Value is not an integer number.\n")],
    ])
    def test_validate_is_int(self, name, value, exp_res):
        act_res = (Validator.validate_is_int(value))
        try:
            self.assertEqual(act_res[0], exp_res[0])
            self.assertEqual(act_res[1], exp_res[1])
        except AssertionError as e:
            msg = "\nFail test - \"{0}\"; Input data - {1}; Error{2}".format(name, value, e)
            raise AssertionError(msg)

    @parameterized.expand([
        ["test_validate_is_float, value - positive number", "12", (True, "Validation successfully.\n")],
        ["test_validate_is_float, value - positive float", "12.324", (True, "Validation successfully.\n")],
        ["test_validate_is_float, value - negative float", "-12.324", (True, "Validation successfully.\n")],
        ["test_validate_is_float, value - null", "0", (True, "Validation successfully.\n")],
        ["test_validate_is_float, value - string", "aaaaa", (False, "Value is not a float number.\n")],
        ["test_validate_is_float, value - number and string", "5a", (False, "Value is not a float number.\n")],
    ])
    def test_validate_is_float(self, name, value, exp_res):
        act_res = (Validator.validate_is_float(value))
        try:
            self.assertEqual(act_res[0], exp_res[0])
            self.assertEqual(act_res[1], exp_res[1])
        except AssertionError as e:
            msg = "\nFail test - \"{0}\"; Input data - {1}; Error{2}".format(name, value, e)
            raise AssertionError(msg)

    @parameterized.expand([
        ["test_validate_file_exists, value - exist file path", "validator_tests.py", (True, "Validation successfully")],
        ["test_validate_file_exists, value - not exist file", "dsdfsd", (False, "File with path dsdfsd not found!")],
        ["test_validate_file_exists, value - blank", "", (False, "File with path  not found!")],
    ])
    def test_validate_file_exists(self, name, value, exp_res):
        act_res = (Validator.validate_file_exists(value))
        try:
            self.assertEqual(act_res[0], exp_res[0])
            self.assertEqual(act_res[1], exp_res[1])
        except AssertionError as e:
            msg = "\nFail test - \"{0}\"; Input data - {1}; Error{2}".format(name, value, e)
            raise AssertionError(msg)

    @parameterized.expand([
        ["test_validate_is_float, value - positive number", "12", (True, "Validation successfully.\n")],
        ["test_validate_is_float, value - number and string", "5a", (False, "Value is not a float number.\n")],
    ])
    def test_validate_is_float(self, name, value, exp_res):
        act_res = (Validator.validate_is_float(value))
        try:
            self.assertEqual(act_res[0], exp_res[0])
            self.assertEqual(act_res[1], exp_res[1])
        except AssertionError as e:
            msg = "\nFail test - \"{0}\"; Input data - {1}; Error{2}".format(name, value, e)
            raise AssertionError(msg)

    def test_single_validate_ok(self):
        act_res = Validator.single_validate({"value": '12.3', "rules": (
            "is_float", "not_null", "not_neg")})
        exp_res = [True, "Validation successfully"]
        self.assertEqual(act_res[0], exp_res[0])
        self.assertEqual(act_res[1], exp_res[1])

    def test_single_validate_not_ok(self):
        act_res = Validator.single_validate({"value": '-4', "rules": (
            "is_int", "not_null", "not_neg")})
        exp_res = [False, "Value is negative.\n"]
        self.assertEqual(act_res[0], exp_res[0])
        self.assertEqual(act_res[1], exp_res[1])


if __name__ == '__main__':
    unittest.main()
