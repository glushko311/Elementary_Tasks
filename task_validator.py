from validator import Validator


class TaskValidator:

    @staticmethod
    def validate_chess_board_tuple(data_tuple: tuple):
        """
        Validate tuple of parameters use Validator methods
        :param data_tuple: (min_value, max_value)
        :return: tuple: (bool, str)
        """
        if len(data_tuple[1]) != 2:
            return False, "Start application with two number parameters!"
        else:
            height = data_tuple[1][0]
            length = data_tuple[1][1]
            validation_height = Validator.single_validate({"value": height, "rules": (
                "is_int", "not_null", "not_neg"
            )})
            validation_length = Validator.single_validate({"value": length, "rules": (
                "is_int", "not_null", "not_neg"
            )})
            if not validation_height[0]:
                return False, "First argument - height is invalid\n" + validation_height[1]
            elif not validation_length[0]:
                return False, "First argument - length is invalid\n" + validation_length[1]
            else:
                return True, "Validation successful"

    @staticmethod
    def validate_envelope_sides(a_side: str, b_side: str):
        validation_a = Validator.single_validate({"value": a_side, "rules": (
            "is_float", "not_null", "not_neg"
        )})
        validation_b = Validator.single_validate({"value": b_side, "rules": (
            "is_float", "not_null", "not_neg"
        )})
        if not validation_a[0]:
            return False, "First argument - height is invalid\n" + validation_a[1]
        elif not validation_b[0]:
            return False, "First argument - length is invalid\n" + validation_b[1]
        else:
            return True, "Validation successful"

    @staticmethod
    def validate_triangular(triang_str: str):
        triang_list = triang_str.split(',')
        if len(triang_list) != 4:
            return False, "Invalid value, value format should be \"name,side_a,side_b,side_c\"."
        if triang_list == "":
            return False, "Name shouldn't be blank."
        for side in triang_list[1:]:
            validate_res = Validator.single_validate({"value": side, "rules": (
                    "is_float", "not_null", "not_neg"
            )})
            if not validate_res[0]:
                return False, "Side validation error.\n" + validate_res[1]
        side_a = float(triang_list[1].strip())
        side_b = float(triang_list[2].strip())
        side_c = float(triang_list[3].strip())
        p = (side_a + side_b + side_c) / 2
        if (p - side_a) * (p - side_b) * (p - side_c) <= 0:
            return False, "It is impossible to create this triangle one of sides too long"
        return True, "Validation successfully"


    @staticmethod
    def validate_fibonachi_tuple(data_tuple: tuple):
        """
        Validate tuple of parameters use Validator methods
        :param data_tuple: (min_value, max_value)
        :return: tuple: (bool, str)
        """
        if len(data_tuple[1]) != 2:
            return False, "Start application with two number parameters!"
        else:
            min_val = data_tuple[1][0]
            max_val = data_tuple[1][1]
            validation_min = Validator.single_validate({"value": min_val, "rules": ("is_int", "not_neg")})
            validation_max = Validator.single_validate({"value": max_val, "rules": ("is_int", "not_neg")})
            if not validation_min[0]:
                return False, "First argument - min_value is invalid\n" + validation_min[1]
            elif not validation_max[0]:
                return False, "First argument - min_value is invalid\n" + validation_max[1]
            else:
                if min_val > max_val:
                    return False, "First parameter(min_value) should be less than second(max_value)!"
                else:
                    return True, "Validation successful"
