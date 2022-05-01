import datetime

class Order:
    def __init__(self, id, cart):
        self.__id = id
        self.__date = datetime.date.today()
        self.cart = cart  # list of {dish: quantity}

    def __str__(self):
        return f'''Order ID:{self.__id:5} Date: {self.__date:12}
                    \r{self.cart}'''