class Dish:
    def __init__(self, name, price):
            self.name = name
            self.price = price

    def __str__(self):
        return f'{self.name:20} VND {self.price}'

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

# dish_0 = Dish('Phở bòa tái', 10)
# dish_1 = Dish('Phở bòa chín', 5)
# dish_2 = Dish('Phở gà sống', 15)
# dish_3 = Dish('Phở DSP', 300)
# dish_4 = Dish('Tea', 1)
# dish_5 = Dish('Soup', 3)

# dishes = [dish_0, dish_1, dish_2, dish_3, dish_4, dish_5]


# # Print a menu of dishes
# def print_menu():
#     print('''\n---------- Menu ----------\n
#             \r**Dish**            **Price**\n''')
#     for dish in dishes:
#         print('', dish)

# print_menu()