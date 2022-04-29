class Dish:
    def __init__(self, name, price):
            self.name = name
            self.price = price

    def __str__(self):
        return f'{self.name:25} {self.price:10}'

    def __repr__(self):
        return f'Dish({self.name}, {self.price})'

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price