import os
from input import *
from domains.Table import *
from domains.M_order import *
from domains.M_dish import *
from domains.M_employee import *

d_manager = Dish_Manager()
e_manager = Employee_Manager()
o_manager = Order_Manager()

table_list = []  # list of tables
for _ in range(0, 9):
    table_list.append(Table())

if __name__ == '__main__':
    if os.path.exists('res_data.zip'):
        try:
            decompress_data()
            d_manager.dishes, d_manager.names = read_data('dishes')
            e_manager.employees, e_manager.ids = read_data('employees')
            # o_manager = read_data('orders')
        except Exception as e:
            print(f'(!) Error: {e}')

    while True:
        os.system('clear')
        password = input('\nEnter password: ')
        while password != 'admin' and password != 'staff':
            if password == 'quit':
                compress_data()
                os.remove('dishes.txt')
                os.remove('employees.txt')
                exit()
            os.system('clear')
            print('(!) Wrong password')
            password = input('Enter password: ')
        if password == 'admin':
            # Administrator section: food menu, employees, and bills
            while True:
                os.system('clear')
                print_admin_action()
                choice = input('\nChoice (1230): ')
                if choice == '0':
                    break
                elif choice == '1':
                    d_manager.start()
                elif choice == '2':
                    e_manager.start()
                elif choice == '3':
                    n = 3

        elif password == 'staff':
            # Staff section: ordering and billing
            while True:
                os.system('clear')
                print_tables(table_list)
                choice = input('\nSelect a table (1-9, 0): ').strip()
                if choice.isdigit() and int(choice) in range(1, 10):
                    table = table_list[int(choice) - 1]  # get the table object
                    if str(table) == '0':  # if table is empty, start ordering for this table
                        table.update()
                        o_manager.add_order(int(choice), d_manager)    # add order with table number

                elif choice == '0':
                    break

        