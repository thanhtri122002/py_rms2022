import os
from domains.Order import Order

def print_cart_order(table, cart):
    print(f'''\n---- Ordering for table {table} -----\n
            \rCart:''')
    if len(cart) == 0:
        print('(!) Empty')
    else:
        for d, q in cart.items():
            print(f'{d}\tx{q}')  # print the cart including name, price and quantity
    print('\n--------------------------------')


class Order_Manager:
    auto_id = 0

    def __init__(self):
        self.__orders = []

    def get_orders(self):
        return self.__orders

    def add_order(self, table_id, dish_manager):
        print(f'\nOrdering for table {table_id}')
        cart = {}   # {dish0: quantity, dish1: quantity, ...}
        dish = dish_manager.get_dishes()
        while len(dish) > 0:    # while there are dishes in the menu
            os.system('clear')
            print_cart_order(table_id, cart)

            print('''\nChoose what to add:
                    \r  1. Add dish
                    \r  2. Edit dish quantity
                    \r  3. Remove dish
                    \r  4. Checkout
                    \r  0. <- Go back''')
            choice = input('\nChoice (12340): ').strip()
            if choice == '0': break
            elif choice == '1':
                print('   Name\t\t\t\tPrice (VND)')
                for i, d in enumerate(dish):
                    print(str(i+1) + '.', d)    # print the menu
                select_dish = input(f'\nChoose a dish to add (1-{len(dish)}, 0): ').strip()
                if select_dish == '0': continue
                elif select_dish.isdigit() and int(select_dish) in range(1, len(dish)+1):
                    dish_name = dish[int(select_dish)-1].get_name()
                    if dish_name in cart:       # if the dish is already in the cart
                        cart[dish_name] += 1    # automatically increase the quantity
                    else:
                        cart[dish_name] = 1     # add selected dish to the cart
            # elif choice == '2':

        self.__orders.append(Order(self.auto_id, cart))