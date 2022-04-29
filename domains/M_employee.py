from input import *
from domains.Employee import Employee

class Employee_Manager:
    ids = []    # List of used IDs
    num_employees = 0

    roles = {'1': 'Manager', '2': 'Chef', '3': 'Waiter',
                '4': 'Receptionist', '5': 'Security Guard'}
    salaries = {'Manager': 7000000, 'Chef': 5000000, 'Waiter': 3000000,
                'Receptionist': 3000000, 'Security Guard': 3000000} 
    shifts = {'1': 'Morning', '2': 'Afternoon', '3': 'Evening'}

    def __init__(self):
        self.__employees = []

    def __str__(self):
        for i in self.__employees:
            print(i)

    def __repr__(self):
        return f'Employee_Manager({self.__employees})'

    def choose_role(self):
        role = input('''. Choose role:
                        \r      1. Manager    2. Chef    3. Waiter
                        \r      4. Receptionist   5. Security Guard
                        \r  Choice (12345): ''').strip()
        while role not in self.roles.keys():
            role = input('(!) Invalid choice\n  Try again (12345): ').strip()
        return self.roles[role]          # Convert from key (12345) to its value

    def choose_shift(self):
        shift = input('''. Choose shift:
                        \r      1. Morning    2. Afternoon    3. Evening
                        \r  Choice (123): ''').strip()
        while shift not in self.shifts.keys():
            shift = input('(!) Invalid choice\n  Try again (123): ').strip()
        return self.shifts[shift]       # Convert from key (123) to its value

    def add_employee(self):
        fst = input('. Enter first name: ')
        lst = input('. Enter last name: ')
        id = input('. Enter ID: ')
        while id in self.ids:
            id = input('(!) This ID is already taken\n Try again: ')
        self.ids.append(id)
        adr = input('. Enter address: ')
        r = self.choose_role()
        salary = self.salaries[r]   # Get the salary of the role
        shift = self.choose_shift()
        self.__employees.append(Employee(fst, lst, id, adr, r, salary, shift))
        self.num_employees += 1

    def edit_employee(self, employee):
        print(f'Editing employee {employee.get_name()}')
        print('''
                \r  1. Name
                \r  2. ID
                \r  3. Address
                \r  4. Role
                \r  5. Shift
                \r  0. Exit''')
        choice = input('\nChoice (123450): ')
        if choice == '0':
            return
        elif choice == '1':
            fst = input('. Enter first name: ')
            lst = input('. Enter last name: ')
            employee.set_name(fst, lst)
        elif choice == '2':
            self.ids.remove(employee.get_id())
            id = input('. Enter ID: ')
            while id in self.ids:
                id = input('(!) This ID is already taken\n Try again: ')
            self.ids.append(id)
            employee.set_id(id)
        elif choice == '3':
            adr = input('. Enter address: ')
            employee.set_address(adr)
        elif choice == '4':
            r = self.choose_role()
            employee.set_role(r)
            employee.set_salary(self.salaries[r])
        elif choice == '5':
            shift = self.choose_shift()
            employee.set_shift(shift)

    def delete_employee(self, employee):
        name = employee.get_name()
        self.__employees.remove(employee)
        self.num_employees -= 1
        self.ids.remove(employee.get_id())
        print(f'Employee {name} are removed')

#

    def list_employees(self):
        # print(self.__employees)
        for i, employee in enumerate(self.__employees):
            print(str(i+1) + '.', employee)

    def list_by_shift(self):
        shift = self.choose_shift()
        print()
        for employee in self.__employees:
            if employee.get_shift() == shift:
                print(employee)

    def list_by_role(self):
        role = self.choose_role()
        print()
        for employee in self.__employees:
            if employee.get_role() == role:
                print(employee)

    def start(self):
        while True:
            print('\n----- Admin / Employee Manager ------\n')
            self.list_employees()
            print('''Choose an option:
                    \r  1. Add employee
                    \r  2. Find employee by ID
                    \r  3. List employees
                    \r  0. Exit''')
            choice0 = input('Choice (123450): ')
            if choice0 == '0':
                return
            elif choice0 in start_menu.keys():
                start_menu[choice0]()
            elif choice0 == '3':
                list_e_menu = { '1': self.list_employees,
                                '2': self.list_by_shift,
                                '3': self.list_by_role }
                while True:
                    print('''\n----- Employee list ------\n
                            \r  1. All
                            \r  2. By shift
                            \r  3. By role
                            \r  0. Go back''')
                    choice1 = input('\nChoice (1230): ')
                    if choice1 == '0':
                        break
                    elif choice1 in list_e_menu.keys():
                        print()
                        list_e_menu[choice1]()
                    else: choice1 = input(f'(!) Invalid choice "{choice1}"\nTry again (1230): ')
            else: choice0 = input(f'(!) Invalid choice "{choice0}"\nTry again (123450): ')