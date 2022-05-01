import datetime

class Order:
    def __init__(self, id, table_id, cart):
        self.__id = id
        self.__table_id = table_id
        self.__date = datetime.date.today()
        self.cart = cart  # list of {dish: quantity}

    def __str__(self):
        return f'''Order ID:{self.__id:5} Date: {self.__date:12} Table: {self.__table_id:1}
                    \r{self.cart}'''