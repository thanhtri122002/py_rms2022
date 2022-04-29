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
        name = input('. Enter name: ')
        while name in self.names:
            name = input('''(!) There is already a dish with this name
                            \r Try again: ''')
        self.names.append(name)
        price = input('. Enter price: ')
        while not price.isdigit or int(price) < 1:
            price = input('''(!) Invalid price
                            \rTry again: ''')
        price = int(price)
        self.__dishes.append(Dish(name, price))
        self.num_dishes += 1

    def edit_dish(self, dish):
        print(f'Editing dish {dish.get_name()}')
        self.names.remove(dish.get_name())
        name = input('. Enter name: ')
        while name in self.names:
            name = input('''(!) There is already a dish with this name
                            \r Try again: ''')
        self.names.append(name)
        price = input('. Enter price: ')
        try:
            while int(price) < 1:
                price = input('''(!) Invalid price
                                \rTry again: ''')
            price = int(price)
        except ValueError:
            print('(!) Invalid input')
        dish.set_name(name)
        dish.set_price(price)

    def delete_dish(self, dish):
        name = dish.get_name()
        self.__dishes.remove(dish)
        self.num_dishes -= 1
        self.names.remove(dish.get_name())
        print(f'Dish \'{name}\' are removed')

    def select_dish(self):
        while True:
            print('\nChoose a dish: ')
            self.list_dishes()
            choice = input(f'Choice (1-{self.num_dishes}, 0 = return): ')
            if choice == '0':
                return 0
            elif choice.isdigit():
                choice = int(choice)
                if choice > 0 and choice <= self.num_dishes:
                    return self.__dishes[choice-1]
                else:
                    print('(!) Invalid input')
            else:
                print('(!) Invalid input')

    def list_dishes(self):
        # print(self.__dishes)
        if self.num_dishes == 0:
            print('(!) No dish\n')
        else:
            for i, dish in enumerate(self.__dishes):
                print(str(i+1) + '.', dish)
            print()

    def start(self):
        while True:
            print('\n----- Admin / Dishes Manager ------\n')
            self.list_dishes()
            print('''Choose an option:
                    \r  1. Add dish
                    \r  2. Edit dish
                    \r  3. Delete dish
                    \r  0. Exit''')
            choice = input('Choice (1230): ')
            if choice == '0':
                return
            elif choice == '1':
                self.add_dish()
            elif choice == '2':
                if self.num_dishes == 0:
                    print('(!) There is no dish')
                else:
                    dish = self.select_dish()
                    if dish == 0:
                        continue
                    self.edit_dish(dish)
            elif choice == '3':
                if self.num_dishes == 0:
                    print('(!) There is no dish')
                else:
                    dish = self.select_dish()
                    if dish == 0:
                        continue
                    self.delete_dish(dish)
            else:
                print('(!) Invalid input')

# d_manager = Dish_Manager()
# d_manager.start()