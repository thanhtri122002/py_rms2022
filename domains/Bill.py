class Bill:
    def __init__(self, table_id):
        self.table_id = table_id
        self.dishes = []    # List of dishes including {dish.name: quantity}
        self.total_price = 0

    def add_dish(self, dish, quantity):
        self.dishes.append({dish.get_name(): quantity})
        self.total_price += dish.get_price() * quantity

    def get_table_id(self):
        return self.table_id

    def get_dishes(self):
        return self.dishes

    def get_total_price(self):
        return self.total_price

    def __str__(self):
        bill = f'\n----- Bill -----\nTable: {self.table_id}\n'
        for dish in self.dishes:
            for key, value in dish.items():
                bill += f'{key:20} x {value}\n'
        bill += f'Total: {self.total_price}\n'
        return bill