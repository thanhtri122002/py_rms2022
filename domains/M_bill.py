from domains.Bill import *

class Bill_Manager:
    auto_id = 0

    def __init__(self):
        self.__bills = []

    def add_bill(self, bill):
        self.__bills.append(bill)

    def get_bills(self):
        return self.__bills