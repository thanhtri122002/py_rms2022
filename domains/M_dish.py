# from input import *
from domains.Dish import Dish

class Dish_Manager:
    names = []  # List of used names
    num_dishes = 0

    def __init__(self):
        self.__dishes = []

    def __str__(self):
        for i in self.__dishes:
            print(i)

    def __repr__(self):
        return f'Dish_Manager({self.__dishes})'

    def add_dish(self):
        print('\nAdding a dish')
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
        self.__dishes.append(Dish(name, price))
        self.num_dishes += 1

    def edit_dish(self, dish):
        while True:
            print(f'\nEditing dish \'{dish.get_name()}\'\n')
            print('''Choose what to edit:
                    \r  1. Name
                    \r  2. Price
                    \r  0. <- Go back''')
            choice = input('Choice (120): ').strip()
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
            else:
                print('(!) Bad choice')

    def delete_dish(self, dish):
        name = dish.get_name()
        self.__dishes.remove(dish)
        self.num_dishes -= 1
        self.names.remove(dish.get_name())
        print(f'Dish \'{name}\' is removed')

    def select_dish(self):
        if self.num_dishes == 0:
            print('(!) There is no dish to modify')
            return 0
        while True:
            choice = input(f'Choose a dish (1-{self.num_dishes}, 0 = return): ').strip()
            if choice == '0':
                return 0
            elif choice.isdigit() and int(choice) in range(1, self.num_dishes+1):
                return self.__dishes[int(choice)-1]
            else:
                print('(!) Bad choice')

    def list_dishes(self):
        # print(self.__dishes)
        if self.num_dishes == 0:
            print('(!) No dish\n')
        else:
            print('   Name\t\t\t\tPrice (VND)')
            for i, dish in enumerate(self.__dishes):
                print(str(i+1) + '.', dish)
            print()

    def start(self):
        while True:
            print('\n----- Admin / Dishes Manager ------\n')
            self.list_dishes()
            print('''-----------------------------------
                    \rChoose an option:
                    \r  1. Add
                    \r  2. Edit
                    \r  3. Delete
                    \r  0. <-- Go back''')
            choice = input('Choice (1230): ').strip()
            if choice == '0':
                return
            elif choice == '1':
                self.add_dish()
            elif choice == '2':
                dish = self.select_dish()
                if dish == 0:
                    continue
                self.edit_dish(dish)
            elif choice == '3':
                dish = self.select_dish()
                if dish == 0:
                    continue
                self.delete_dish(dish)
            else:
                print('(!) Bad choice')

if __name__ == '__main__':
    dish_manager = Dish_Manager()
    dish_manager.start()