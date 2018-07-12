class Validator:

    @staticmethod
    def validate_positive_not_null(side: str):
        """
        validate data return tuple with True False and message
        :return:Envelope
        """
        if not side.isdigit():
            return False, "Input value is not number"
        if float(side) <= 0:
            return False, "Input value is null or negative"
        return True, "Validation successfully"
