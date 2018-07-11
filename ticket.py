class Ticket(object):
    '''
    Class describe ticket instance
    Parameters:
        __ticket_num
    Methods:
        is_happy_moskow
        is_happy_piter
        __repr__
    '''
    def __init__(self, ticket_num):
        self.__ticket_num = ticket_num

    @property
    def ticket_num(self):
        return self.__ticket_num

    @staticmethod
    def get_n_validate():
        ticket_num = input()
        return len(ticket_num) == 6 and ticket_num.isdigit()

    def __is_happy_moskow(self):
        '''
        Calculate is this ticket happy by Moscow algorithm
        :return: bool
        '''
        t = self.__ticket_num
        left = 0
        right = 0
        for i in range(len(t)):
            if (i+1) <= (len(t) // 2):
                left += int(t[i])
            else:
                right += int(t[i])
        return left == right

    def __is_happy_piter(self):
        '''
            Calculate is this ticket happy by Pitersburg algorithm
            :return: bool
        '''
        even = 0
        odd = 0
        t = self.__ticket_num
        for i in range(0, len(t)):
            if (i+1) % 2 == 0:
                odd += int(t[i])
            else:
                even += int(t[i])
        return even == odd

    def __repr__(self):
        return self.__ticket_num

    def is_happy(self, mark: str):
        if mark == "Moscow":
            return self.__is_happy_moskow()
        elif mark == "Piterburg":
            return self.__is_happy_piter()
