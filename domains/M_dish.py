import os
from input import *
from domains.Dish import Dish

class Dish_Manager:
    names = []  # List of used names
    num_dishes = 0

    def __init__(self):
        self.dishes = []

    def __str__(self):
        for i in self.dishes:
            print(i)

    def add_dish(self):
        os.system('clear')
        print('''\n----- Admin / Dishes Manager ------\n
                \rAdding a dish''')
        name = input('. Enter name: ').strip()
        while name in self.names or name == '':
            if name == '':
                name = input('''(!) Invalid name
                            \rTry again: ''').strip()
            else:
                name = input(f'''(!) There is a \'{name}\' already
                            \r Try again: ''').strip()
        self.names.append(name)
        price = input('. Enter price: ').strip()
        while not price.isdigit() or int(price) < 1:
            price = input('''(!) Invalid price
                            \rTry again: ''').strip()
        price = int(price)
        self.dishes.append(Dish(name, price))

    def edit_dish(self, dish):
        while True:
            os.system('clear')
            print('\n---- Admin / D_Manager / Edit -----\n')
            print(f'''Name\t\t\t     Price (VND)
                    \r{dish}\n
                    \r-----------------------------------''')
            print('''\nChoose what to edit:
                    \r  1. Name
                    \r  2. Price
                    \r  0. <- Go back''')
            choice = input('\nChoice (120): ').strip()
            if choice == '0':
                return
            elif choice == '1':
                self.names.remove(dish.get_name())
                name = input('. Enter name: ').strip()
                while name in self.names:
                    name = input('''(!) There is already a dish with this name
                                    \r Try again: ''').strip()
                dish.set_name(name)
                self.names.append(name)
            elif choice == '2':
                price = input('. Enter price: ').strip()
                try:
                    while not price.isdigit() or int(price) < 1:
                        price = input('''(!) Invalid price
                                        \rTry again: ''').strip()
                    price = int(price)
                except ValueError:
                    print('(!) Invalid input')
                dish.set_price(price)

    def delete_dish(self, dish):
        self.names.remove(dish.get_name())
        self.dishes.remove(dish)

    def select_dish(self, action):
        if len(self.dishes) == 0: return 0
        while True:
            os.system('clear')
            print('\n----- Admin / Dishes Manager ------\n')
            self.list_dishes()
            print('''0. <-- Go back
                    \r-----------------------------------''')
            choice = input(f'\nChoose a dish to {action} (1-{len(self.dishes)}, 0): ').strip()
            if choice == '0':
                return 0
            elif choice.isdigit() and int(choice) in range(1, len(self.dishes)+1):
                return self.dishes[int(choice)-1]

    def list_dishes(self):
        # print(self.dishes)
        if len(self.dishes) == 0:
            print('(!) No dish')
        else:
            print('   Name\t\t\t\tPrice (VND)')
            for i, dish in enumerate(self.dishes):
                print(str(i+1) + '.', dish)

    def start(self):
        while True:
            write_data('dishes', self.dishes, self.names)
            os.system('clear')
            print('\n----- Admin / Dishes Manager ------\n')
            self.list_dishes()
            print('''\n-----------------------------------
                    \r\nChoose an option:
                    \r  1. Add
                    \r  2. Edit
                    \r  3. Delete
                    \r  0. <-- Go back''')
            choice = input('\nChoice (1230): ').strip()
            if choice == '0':
                os.system('clear')
                return
            elif choice == '1':
                self.add_dish()
            elif choice == '2':
                dish = self.select_dish('edit')
                if dish == 0:
                    continue
                self.edit_dish(dish)
            elif choice == '3':
                dish = self.select_dish('delete')
                if dish == 0:
                    continue
                self.delete_dish(dish)

if __name__ == '__main__':
    dish_manager = Dish_Manager()
    dish_manager.start()