import re
import os


class Validator:
    """
    Universal validator you can use method single validate send there value and rules in list
    """

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
    def validate_is_int(value: str):
        """
        Validate parameter is it can be convert into integer
        :param value:
        :return:
        """
        if not re.match(r'^\s*[-+]?\d*\s*$', value):
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
        {'value':value, 'rules':("is_int", "not_null")
        """
        for short_code in validate_pack['rules']:
            func = getattr(Validator, Validator.SHORT_CODES[short_code])
            valid_res = func(validate_pack['value'])
            if not valid_res[0]:
                return False, valid_res[1]

        return True, "Validation successfully"
