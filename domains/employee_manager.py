from input import input_num
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
                        \r  Choice (12345): ''')
        while role not in self.roles.keys():
            role = input('(!) Invalid choice\n  Try again (12345): ')
        return self.roles[role]          # Convert from key (12345) to its value

    def choose_shift(self):
        shift = input('''  Choose shift:
                        \r      1. Morning    2. Afternoon    3. Evening
                        \r  Choice (123): ''')
        while shift not in self.shifts.keys():
            shift = input('(!) Invalid choice\n  Try again (123): ')
        return self.shifts[shift]       # Convert from key (123) to its value

    def add_employee(self):
        n = input_num('employees')
        for i in range(n):
            print(f'\n----- Employee {i + 1} of {n} -----\n')
            fst = input('. Enter first name: ')
            lst = input('. Enter last name: ')

            id = input('. Enter ID: ')
            while id in self.ids:
                id = input('(!) This ID is already taken\nEnter ID: ')
            self.ids.append(id)

            adr = input('. Enter address: ')
            r = self.choose_role()
            salary = self.salaries[r]   # Get the salary of the role
            shift = self.choose_shift()
            self.__employees.append(Employee(fst, lst, id, adr, r, salary, shift))
            self.num_employees += 1

    def delete_employee(self, employee):
        name = employee.get_name()
        self.__employees.remove(employee)
        self.num_employees -= 1
        self.ids.remove(employee.get_id())
        print(f'Employee {name} are removed')

    def find_by_id(self):
        id = input('Enter ID: ')
        while id not in self.ids:
            id = input('(!) There is no employee with this ID\nEnter again ID: ')
        for employee in self.__employees:
            if employee.get_id() == id:
                return employee

    def list_employees(self):
        print(self.__employees)

    def list_by_shift(self):
        shift = self.choose_shift()
        for employee in self.__employees:
            if employee.get_shift() == shift:
                print(employee)

    def list_by_role(self):
        role = self.choose_role()
        for employee in self.__employees:
            if employee.get_role() == role:
                print(employee)

    def start(self):
        while True:
            start_menu = {  '1': self.add_employee,
                            '2': self.find_by_id }
            print('''\n----- Employee Manager ------\n
                    \r  1. Add employee
                    \r  2. Find employee by ID
                    \r  3. List employees
                    \r  0. Exit''')
            choice0 = input('\nChoice (123450): ')
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