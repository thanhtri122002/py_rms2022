from domains.M_dish import Dish_Manager
from domains.M_employee import *

d_manager = Dish_Manager()
e_manager = Employee_Manager()

if __name__ == '__main__':
    while True:
        password = input('\nEnter password: ')
        if password == 'admin':
            # Administrator section: food menu, employees, and bills
            while True:
                print('''\n--------- Administrator ---------\n
                        \r  1. Dishes
                        \r  2. Employees
                        \r  3. Bills
                        \r  0. Quit''')
                choice = input('\nChoice (1230): ')
                if choice == '0':
                    break
                elif choice == '1':
                    d_manager.start()
                elif choice == '2':
                    e_manager.start()
                elif choice == '3':
                    n = 3
                else:
                    print('(!) Bad choice')

        elif password == 'staff':
            # Staff section: ordering and billing
            while True:
                print('''\n----- Tables -----\n
                        \r  đang làm''')
                choice = input('\nẤn 0 để sủi: ')
                if choice == '0':
                    break
                else: 
                    print(f'\'{choice}\' là cái đéo gì')
        else:
            print('(!) Wrong password')