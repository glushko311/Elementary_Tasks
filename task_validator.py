from validator import Validator


class TaskValidator:

    @staticmethod
    def validate_fibonachi_tuple(data_tuple):
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