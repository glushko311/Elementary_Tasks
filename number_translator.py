from optparse import OptionParser


class NumberTranslator:
    '''
    Contain methods to translate number into text display
    '''
    __DICT_NUMBERS = {
        '-': {'-': "минус"},
        0: {0: "ноль"},
        1: {
            1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть",
            7: "семь", 8: "восемь", 9: "девять", 0: ""
        },
        10: {
            1: "десять", 2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят",
            6: "шестьдесят", 7: "семьдесят", 8: "восемьдесят", 9: "девяносто"
        },
        100: {
            1: "сто", 2: "двести", 3: "триста", 4: "четыреста", 5: "пятьсот",
            6: "шестьсот", 7: "семьсот", 8: "восемьсот", 9: "девятсот"
        },
        "teen": {
            10: "десять", 11: "одинадцать", 12: "двенадцать", 13: "тринадцать",
            14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать",
            18: "восемнадцать", 19: "девятнадцать"
        },
        1000: {
            1: "ча", 2: "чи", 3: "чи", 4: "чи", 5: "ч", 6: "ч", 7: "ч", 8: "ч",
            9: "ч", 0: "ч"
        },

        "million": {
            1: "", 2: "а", 3: "а", 4: "а", 5: "ов",
            6: "ов", 7: "ов", 8: "ов", 9: "ов", 0: "ов"
        },
        "large_names": {
            2: "миллион", 3: "миллиард", 4: "триллион", 5: "квадриллион", 6: "квинтиллион",
            7: "секстиллион", 8: "септиллион", 9: "октиллион", 10: "нониллион",
            11: "дециллион", 12: "андециллион", 13: "дуодециллион",
            14: "тредециллион", 15: "кваттордециллион", 16: "квиндециллион",
            17: "сексдециллион", 18: "септемдециллион", 19: "октодециллион",
            20: "новемдециллион", 21: "вигинтиллион", 22: "анвигинтиллион",
            23: "дуовигинтиллион", 24: "тревигинтиллион", 25: "кватторвигинтиллион",
            26: "квинвигинтиллион", 27: "сексвигинтиллион", 28: "септемвигинтиллион",
            29: "октовигинтиллион", 30: "новемвигинтиллион", 31: "тригинтиллион",
            32: "антригинтиллион", 33: "гугол"
        }
    }

    def __from_1_to_99(self, num: int) -> str:
        '''
        translate numbers from 1 to 99 into text
        :param num:
        :return:
        '''
        dict_numbers = self.__DICT_NUMBERS
        if num == 0:
            res_str = ""
        elif 1 <= num <= 9:
            res_str = dict_numbers[1][num]
        elif 10 <= num <= 19:
            res_str = dict_numbers['teen'][num]
        else:
            res_str = "" + dict_numbers[10][num // 10] + " " + dict_numbers[1][num % 10]
        return res_str

    def __from_99_to_999(self, num: int) -> str:
        '''
        Translate numbers from 99 to 999 into text
        :param num:
        :return:
        '''
        dict_numbers = self.__DICT_NUMBERS
        if num <= 99:
            return self.__from_1_to_99(num)
        return dict_numbers[100][num // 100] + " " + self.__from_1_to_99(num % 100)

    def __get_thousands(self, num: int) -> str:
        '''
        Translate numbers from 999 to 999 999 into text
        :param num:
        :return:
        '''
        dict_numbers = self.__DICT_NUMBERS
        res_str = ""
        num_thousands = num // 1000

        if (10 <= num_thousands) and (10 <= (int((str(num_thousands))[-2] + (str(num_thousands))[-1])) <= 19):
            # two_last_digits = int((str(num_thousands))[-2] + (str(num_thousands))[-1])
            thousand = self.__from_99_to_999(num_thousands) + " тысяч"
        else:
            last_digit = int((str(num_thousands))[-1])
            thousand = self.__from_99_to_999(num_thousands) + \
                       " тыся" + dict_numbers[1000][last_digit]

        thousand = thousand.replace("один ", "одна ")
        thousand = thousand.replace("два ", "две ")
        res_str += thousand + " " + \
                   self.__from_99_to_999(num % 1000)
        return res_str

    def __number_handler(self, num: int) -> str:
        '''
        Main converter from number into string
        :param num:
        :return:
        '''
        dict_numbers = self.__DICT_NUMBERS
        if num > ((10 ** 102) - 1):
            print("Вы ввели слишком большое число!")
            quit()
        res_str = ""
        if num < 0:
            num = abs(num)
            res_str += dict_numbers['-']['-'] + " "
        if 0 <= num <= 999:
            res_str += self.__from_99_to_999(num)
        elif 1 <= num // 1000 <= 999:
            res_str = self.__get_thousands(num)
        else:
            arr_number = []
            arr_item = []
            count = 0

            for i in str(num)[::-1]:
                if count < 3:
                    arr_item.append(i)
                    count += 1
                else:
                    count = 1
                    arr_number.append(arr_item)
                    arr_item = []
                    arr_item.append(i)
            arr_number.append(arr_item)
            for i in range(len(arr_number) - 1, 1, -1):

                three_digits = int("".join((arr_number[i])[::-1]))
                last_digit = int((str(three_digits))[-1])
                if three_digits != 0:
                    res_str += self.__number_handler(three_digits) + " "
                    res_str += dict_numbers['large_names'][i]

                    if (10 <= three_digits) and (10 <= (int((str(three_digits))[-2] + (str(three_digits))[-1])) <= 19):
                        res_str += "ов "
                    else:
                        res_str += dict_numbers["million"][last_digit] + " "

            res_str += self.__number_handler(int("".join((arr_number[0] + arr_number[1])[::-1]))) + " "
        return res_str

    def translate(self, num: int) -> str:
        '''
        Check number by null and strip spaces in text appearence
        :param num:
        :return:
        '''
        if num == 0:
            res_str = self.__DICT_NUMBERS[0][0]
        else:
            res_str = self.__number_handler(num)
        return res_str.strip()


def start():
    parser = OptionParser()
    args = parser.parse_args()

    number = 0
    try:
        number = int(args[1][0])
    except IndexError:
        print("Введите параметр - число в интервале (-10**102 .. 10**102)")
        quit()
    except ValueError:
        print("Введите параметр - число в интервале (-10**102 .. 10**102)")
        quit()

    number_translator = NumberTranslator()

    print(number_translator.translate(number))


if __name__ == "__main__":
    start()
