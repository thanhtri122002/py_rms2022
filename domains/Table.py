from tkinter import N
from input import *

class Table:
    def __init__(self):
        self.__status = 0
        self.__order = None     # Order object

    def __str__(self):
        return f'{self.__status}'

    def update(self):
        if self.__status == 0:
            self.__status = 1
        else: self.__status = 0

    def push_order(self, order):
        self.__order = order
        