import os
from input import *
from domains.M_dish import Dish_Manager
from domains.M_employee import *

d_manager = Dish_Manager()
e_manager = Employee_Manager()

if __name__ == '__main__':
    while True:
        os.system('clear')
        password = input('\nEnter password: ')
        while password != 'admin' and password != 'staff':
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
                print('''\n----- Tables -----\n
                        \r  đang làm''')
                choice = input('\nẤn 0 để sủi: ')
                if choice == '0':
                    break