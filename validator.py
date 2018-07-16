import re


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
        "is_triang": "validate_is_triangular_input"
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



# deprecated methods need to refactor!
#     @staticmethod
#     def validate_positive_not_null(str_num: str):
#         """
#         validate data return tuple with True False and message
#         :return: bool, msg: str
#         """
#         if not str_num.isdigit():
#             return False, "Value is not a number"
#         if int(str_num) <= 0:
#             return False, "Value is null or negative"
#         return True, "Validation successfully"
#
#     @staticmethod
#     def validate_int_null(str_num: str):
#         """
#         validate data return tuple with True False and message
#         :return: bool, msg: str
#         """
#         if not str_num.isdigit():
#             return False, "Value is not a number"
#         if int(str_num) < 0:
#             return False, "Value is negative"
#         return True, "Validation successfully"
#
#     @staticmethod
#     def validate_float_not_null(str_num: str):
#         if not re.match(r'\s*\d*\.?\d*\s*', str_num):
#             return False, "Value is not number"
#         if float(str_num) <= 0:
#             return False, "Value is null or negative"
#         else:
#             return True, "Validation successfully"
#
#     @staticmethod
#     def validate_two_float_not_null(str_num1: str, str_num2: str):
#         res1 = Validator.validate_float_not_null(str_num1)
#         res2 = Validator.validate_float_not_null(str_num2)
#         if res1[0] and res2[0]:
#             return True, "Validation successfully"
#         msg = ""
#         if not res1[0]:
#             msg += "First value not valid.\n"
#         if not  res2[0]:
#             msg += "Second value not valid.\n"
#         msg += "Value should be positive not null number."
#         return False, msg
#
#     @staticmethod
#     def validate_two_int_not_null(str_num1: str, str_num2: str):
#         res1 = Validator.validate_positive_not_null(str_num1)
#         res2 = Validator.validate_positive_not_null(str_num2)
#         if res1[0] and res2[0]:
#             return True, "Validation successfully"
#         msg = ""
#         if not res1[0]:
#             msg += "First value not valid.\n"
#         if not res2[0]:
#             msg += "Second  value not valid.\n"
#         msg += "Value should be positive not null number."
#         return False, msg
#
#     @staticmethod
#     def validate_two_int_null(str_num1: str, str_num2: str):
#         res1 = Validator.validate_positive_not_null(str_num1)
#         res2 = Validator.validate_positive_not_null(str_num2)
#         if res1[0] and res2[0]:
#             return True, "Validation successfully"
#         msg = ""
#         if not res1[0]:
#             msg += "First value not valid.\n"
#         if not res2[0]:
#             msg += "Second value not valid.\n"
#         msg += "Value should be positive not null number."
#         return False, msg

    @staticmethod
    def validate_triangular(input_data: str):
        """
        get data and validate
        :return: Triangular
        """
        from triangular import Triangular
        from exceptions.triangular_exception import TriangularException

        if not re.match(r'\w+\s*,\s*\d*\.?\d*\s*,\s*\d*\.?\d*\s*,\s*\d*\.?\d*', input_data):
            raise TriangularException("Not valid input format should be - name,side_a,side_b,side_c")

        data_list = input_data.split(',')
        name = data_list[0].strip()
        side_a = float(data_list[1].strip())
        side_b = float(data_list[2].strip())
        side_c = float(data_list[3].strip())

        p = (side_a + side_b + side_c) / 2

        if (p - side_a) * (p - side_b) * (p - side_c) <= 0:
            raise TriangularException('It is impossible to create this triangle '
                                      'one of sides too long')
        square = (p * (p - side_a) * (p - side_b) * (p - side_c)) ** 0.5
        return Triangular(side_a, side_b, side_c, square, name)

    @staticmethod
    def validate_min_max_values_tuple(min_max_tuple):
        if len(min_max_tuple) != 2:
            return False, "Application need two parameters."

