class Table:
    def __init__(self):
        self.__status = 0

    def __str__(self):
        return f'{self.__status}'

    def update(self):
        if self.__status == 0:
            self.__status = 1
        else: self.__status = 0