import os
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

    def choose_role(self):
        role = input('''. Choose role:
                        \r      1. Manager    2. Chef     3. Waiter
                        \r      4. Receptionist   5. Security Guard
                        \r  Choice (12345): ''').strip()
        while role not in self.roles.keys():
            role = input('(!) Bad choice\n  Try again (12345): ').strip()
        return self.roles[role]          # Convert from key (12345) to its value

    def choose_shift(self):
        shift = input('''. Choose shift:
                        \r     1. Morning   2. Afternoon   3. Evening
                        \r  Choice (123): ''').strip()
        while shift not in self.shifts.keys():
            shift = input('(!) Bad choice\n  Try again (123): ').strip()
        return self.shifts[shift]       # Convert from key (123) to its value

    def add_employee(self):
        os.system('clear')
        print('''\n---- Admin / Employee Manager -----\n
                \rAdding an employee''')
        fst, lst = input_name()
        id = input('. Enter ID: ').strip()
        while id in self.ids:
            id = input('(!) This ID is already taken\n Try again: ').strip()
        self.ids.append(id)
        adr = input('. Enter address: ').strip()
        r = self.choose_role()
        salary = self.salaries[r]   # Get the salary of the role
        shift = self.choose_shift()
        self.__employees.append(Employee(fst, lst, id, adr, r, salary, shift))
        self.num_employees += 1

    def edit_employee(self, employee):
        while True:
            os.system('clear')
            print('\n---- Admin / E_Manager / Edit -----\n')
            print(f'''Name\t\t\t  ID\t\t  Address\t  Role\t\t      Salary  Shift
                    \r{employee}\n
                    \r-----------------------------------''')
            print('''\nChoose what to edit:
                    \r  1. Name
                    \r  2. ID
                    \r  3. Address
                    \r  4. Role
                    \r  5. Shift
                    \r  0. <-- Go back''')
            choice = input('\nChoice (123450): ').strip()
            if choice == '0':
                return
            elif choice == '1':
                fst, lst = input_name()
                employee.set_name(fst, lst)
            elif choice == '2':
                self.ids.remove(employee.get_id())
                id = input('. Enter ID: ').strip()
                while id in self.ids:
                    id = input('(!) This ID is already taken\n Try again: ').strip()
                employee.set_id(id)
                self.ids.append(id)
            elif choice == '3':
                adr = input('. Enter address: ').strip()
                employee.set_address(adr)
            elif choice == '4':
                r = self.choose_role()
                employee.set_role(r)
                employee.set_salary(self.salaries[r])
            elif choice == '5':
                shift = self.choose_shift()
                employee.set_shift(shift)

    def delete_employee(self, employee):
        self.ids.remove(employee.get_id())
        self.__employees.remove(employee)
        self.num_employees -= 1

    def select_employee(self, action):
        if self.num_employees == 0: return 0
        while True:
            os.system('clear')
            print('\n---- Admin / Employee Manager -----\n')
            self.list_employees()
            print('''0. <-- Go back
                    \r-----------------------------------''')
            choice = input(f'\nSelect an employee to {action} (1-{self.num_employees}, 0): ').strip()
            if choice == '0':
                return 0
            elif choice.isdigit() and int(choice) in range(1, self.num_employees+1):
                return self.__employees[int(choice)-1]

    def list_employees(self):
        # print(self.__employees)
        if self.num_employees == 0:
            print('(!) No employees')
        else:
            print('   Name\t\t\t     ID\t\t     Address\t     Role\t\t Salary  Shift')
            for i, employee in enumerate(self.__employees):
                print(str(i+1) + '.', employee)

    def list_by_shift(self):
        shift = self.choose_shift()
        print()
        for employee in self.__employees:
            if employee.get_shift() == shift:
                print(employee)

    def start(self):
        while True:
            os.system('clear')
            print('\n---- Admin / Employee Manager -----\n')
            self.list_employees()
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
                self.add_employee()
            elif choice == '2':
                employee = self.select_employee('edit')
                if employee == 0:
                    continue
                self.edit_employee(employee)
            elif choice == '3':
                employee = self.select_employee('delete')
                if employee == 0:
                    continue
                self.delete_employee(employee)

if __name__ == '__main__':
    e_manager = Employee_Manager()
    e_manager.start()