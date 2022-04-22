class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        ingredients = []
        n = input('Enter ingredients separated by commas ",": ')
        for i in n.split(","):
            ingredients.append(i)
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name} - {self.price} - {self.ingredients}"

    def __repr__(self):
        return f"{self.name} - {self.price} - {self.ingredients}"

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.ingredients == other.ingredients

    def __hash__(self):
        return hash(self.name)