from optparse import OptionParser

from task_validator import TaskValidator


class FileHandler:
    """
    Contain methods to work with file
    """

    @staticmethod
    def find_n_count(file_path: str, substring: str):
        """
        Count number of substrings in the file
        :param file_path: str
        :param substring: str
        :return:
        """
        with open(file_path, "r") as f:
            text = f.read()
        return text.count(substring)

    @staticmethod
    def find_n_replace(file_path: str, old_str: str, new_str: str):
        """
        Replace one substring to another in the file
        :param file_path:
        :param old_str:
        :param new_str:
        :return:
        """
        with open(file_path, 'r') as f:
            text = f.read()
        new_text = text.replace(old_str, new_str)
        with open(file_path, 'w') as f:
            f.write(new_text)


def start():
    """
    Start application function
    :return:
    """
    parser = OptionParser()
    args = parser.parse_args()
    valid_res = TaskValidator.validate_file_handler(args)
    if valid_res[0]:
        path = args[1][0]
        if len(args[1]) == 3:
            old_str = args[1][1]
            new_str = args[1][2]
            FileHandler.find_n_replace(path, old_str, new_str)
        elif len(args[1]) == 2:
            substr = args[1][1]
            substr_in_file = FileHandler.find_n_count(path, substr)
            print("The file by path \'{0}\' contain {1}, substrings \'{2}\'.".
                  format(path, substr_in_file, substr))
    else:
        print(valid_res[1])


if __name__ == "__main__":
    start()
