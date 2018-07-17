import re
import os


class Validator:

    @staticmethod
    def validate_is_not_null(value):
        """
        Validate parameter is it null
        :param value:
        :return:
        """
        if float(value) == 0:
            return False, "Value is null.\n"
        else:
            return True, "Validation successfully.\n"

    @staticmethod
    def validate_is_not_negative(value):
        """
        Validate parameter is it negative
        :param value:
        :return:
        """
        if float(value) < 0:
            return False, "Value is negative.\n"
        else:
            return True, "Validation successfully.\n"

    @staticmethod
    def validate_is_int(value):
        """
        Validate parameter is it can be convert into integer
        :param value:
        :return:
        """
        if not value.isdigit():
            return False, "Value is not an integer number.\n"
        else:
            return True, "Validation successfully.\n"

    @staticmethod
    def validate_is_float(value):
        """
        Validate parameter is it can be convert into float
        :param value:
        :return:
        """
        if not re.match(r'^\s*[-+]?\d*\.?\d*\s*$', value):
            return False, "Value is not a float number.\n"
        else:
            return True, "Validation successfully.\n"

    @staticmethod
    def validate_file_exists(value):
        """
        Validate is exists file with path value
        :param value:
        :return:
        """
        if os.path.isfile(value):
            return True, "Validation successfully"
        else:
            return False, "File with path {0} not found!".format(value)
    #
    # @staticmethod
    # def validate_is_triangular_input(value):
    #     """
    #     Validate parameter is it can be convert into triangular use regular expressions
    #     :param value:
    #     :return:
    #     """
    #     if not re.match(r'^\w+\s*,\s*\d*\.?\d*\s*,\s*\d*\.?\d*\s*,\s*\d*\.?\d*$', value):
    #         return False, "Incorrect triangular input data (should be \"name,side_a,side_b,side_c\")"
    #     else:
    #         return True, "Validation successfully.\n"

    SHORT_CODES = {
        "not_null": "validate_is_not_null",
        "not_neg": "validate_is_not_negative",
        "is_int": "validate_is_int",
        "is_float": "validate_is_float",
        "file_exists": "validate_file_exists"

    }

    @staticmethod
    def single_validate(validate_pack: dict):
        """
        Validate one value validate_pack['value'] by rules from validate_pack['rules']
        validation_pack it is tuple with value and tuple of validation rules
        """
        for short_code in validate_pack['rules']:
            func = getattr(Validator, Validator.SHORT_CODES[short_code])
            valid_res = func(validate_pack['value'])
            if not valid_res[0]:
                return False, valid_res[1]

        return True, "Validation successfully"

    @staticmethod
    def validate_min_max_values_tuple(min_max_tuple):
        if len(min_max_tuple) != 2:
            return False, "Application need two parameters."
