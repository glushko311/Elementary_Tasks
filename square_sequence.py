from optparse import OptionParser

from task_validator import TaskValidator


class Sequence:
    """
    Class to create save and print sequences
    """
    def __init__(self, sequence):
        self.sequence = sequence

    def __str__(self):
        return ", ".join(self.sequence)

    @staticmethod
    def start():
        """
        Start application function
        :return:
        """
        parser = OptionParser()
        args = parser.parse_args()
        validate_res = TaskValidator.validate_sequence(args)
        if validate_res[0]:
            num = int(args[1][0])
            sequence = Sequence([str(i) for i in range(1, num**2) if i**2 < num])
            print(sequence)
        else:
            print(validate_res[1])
            
        
if __name__ == "__main__":
    Sequence.start()
