from input import *

class Table:
    def __init__(self, status = 0):
        self.__status = status

    def __str__(self):
        return f'{self.__status}'

    def update(self):
        if self.__status == 0:
            self.__status = 1
        else: self.__status = 0