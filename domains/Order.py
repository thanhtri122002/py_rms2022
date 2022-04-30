import datetime

class Order:
    def __init__(self, id, carts):
        self.id = id
        self.date = datetime.date.today()
        self.carts = carts  # list of {dish: quantity}

    def __str__(self):
        return f'''Order ID:{self.id:5} Date: {self.date:12}
                    \r{self.carts}'''