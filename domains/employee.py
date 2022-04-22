class Employee:
    def __init__(self,)->None:
        self.__first = ""
        self.__last = ""
        self.__id = ""
        self.__address = ""
        self.__job =""
        self.__salary = 0
        self.__shift = ""
        
    def set_first(self, first):
        self.__first = first

    def get_first(self):
        return self.__first
    
    def set_last(self, last):
        self.__last = last
    
    def get_last(self):
        return self.__last
    
    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id
    
    def set_address(self, address):
        self.__address = address
    
    def get_address(self):
        return self.__address
    
    def set_job(self, job):
        self.__job = job
    
    def get_job(self):
        return self.__job

    def set_salary(self, salary):
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    def set_shift(self, shift):
        self.__shift = shift
    
    def get_shift(self):
        return self.__shift
    
    def get_full_name(self):
        return f"{self.__first} {self.__last}"
    
    def input_info(self):
        self.set_first(input("Enter first name: "))
        self.set_last(input("Enter last name: "))
        self.set_id(input("Enter ID: "))
        self.set_address(input("Enter address: "))
        self.set_job(input("Enter job: "))
        self.set_salary(input("Enter salary: "))
        self.set_shift(input("Enter shift: "))

    def __str__(self):
        return f"{self.get_full_name()} {self.get_id()} lives at {self.get_address()} working as {self.get_job()} which has {self.get_salary()} is payed ativing in shift {self.get_shift()}"

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



