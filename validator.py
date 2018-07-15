import re

class Validator:

    @staticmethod
    def validate_positive_not_null(str_num: str):
        """
        validate data return tuple with True False and message
        :return: bool, msg: str
        """
        if not str_num.isdigit():
            return False, "Input value is not number"
        if float(str_num) <= 0:
            return False, "Input value is null or negative"
        return True, "Validation successfully"

    @staticmethod
    def validate_float_not_null(str_num: str):
        if not re.match(r'\s*\d*\.?\d*\s*', str_num):
            return False, "Input value is not number"
        if float(str_num) <= 0:
            return False, "Input value is null or negative"
        else:
            return True, "Validation successfully"

    @staticmethod
    def validate_two_float_not_null(str_num1: str, str_num2: str):
        res1 = Validator.validate_float_not_null(str_num1)
        res2 = Validator.validate_float_not_null(str_num2)
        if res1[0] and res2[0]:
            return True, "Validation successfully"
        msg = ""
        if not res1[0]:
            msg += "First input value not valid.\n"
        if not  res2[0]:
            msg += "Second input value not valid.\n"
        msg += "Input value should be positive not null number."
        return False, msg


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
        print(side_a)
        print(side_b)
        print(side_c)
        p = (side_a + side_b + side_c) / 2

        if (p - side_a) * (p - side_b) * (p - side_c) <= 0:
            raise TriangularException('It is impossible to create this triangle '
                                      'one of sides too long')

        square = (p * (p - side_a) * (p - side_b) * (p - side_c)) ** 0.5
        return Triangular(side_a, side_b, side_c, square, name)

