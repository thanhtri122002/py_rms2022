import datetime

class Bill:
    def __init__(self, id, table_id, cart, total_price):
        self.__id = id
        self.__table_id = table_id
        self.__cart = cart
        self.__total_price = 0
        self.__date = datetime.datetime.now()

    def get_id(self):
        return self.__id

    def get_table_id(self):
        return self.__table_id

    def get_cart(self):
        return self.__cart

    def get_total_price(self):
        return self.__total_price

    def get_date(self):
        return self.__date

    def __str__(self):
        return f'{self.__date: %d/%m/%Y}\t{self.__total_price}'

    def detail(self, dishes):
        bill = f'''\n----------------- Bill -----------------\n
        \rTable: {self.__table_id}              ID: {self.__id}
        \rTime: {self.__date: %d/%m/%Y %H:%M}\n'''
        for d, q in self.__cart.items():
            for dish in dishes:
                if dish.get_name() == d:
                    bill += f'{dish} x {q}\n'

        bill += f'''\n*** Total: {self.__total_price} ***
                \n----------------------------------------'''
        return bill

    def start(self):
        pass