from domains.Employee import Employee

class EmployeeManagement:
    def __init__(self)->None:
        self.__employees = []

    def quantities(self):
        quantities = int(input("Enter the number of employees: "))
        return quantities

    def add_employee(self):
        for i in range(self.quantities()):
            employee = Employee()
            employee.input_info()
            self.__employees.append(employee)

    def search_by_id(self):
        id = input("Enter the ID: ")
        for e in self.__employees:
            if e.get_id() == id:
                print(e)
                return 
            else:
                continue
        if e.get_id() != id:
            print("ID not found")

    def list_by_shift(self):
        shift = input("Enter the shift: ")
        for e in self.__employees:
            if e.get_shift() == shift:
                print(e)

    def list_by_job(self):
        job = input("Enter the job: ")
        for e in self.__employees:
            if e.get_job() == job:
                print(e)

    def print_employees(self):
        for e in self.__employees:
            print('\n')
            print(e)