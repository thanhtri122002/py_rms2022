class Employee:
    def __init__(self, first, last, id, address, role, salary, shift):
        self.__first = first
        self.__last = last
        self.__id = id
        self.__address = address
        self.__role = role
        self.__salary = salary
        self.__shift = shift

    def set_name(self, first, last):
        self.__first = first
        self.__last = last

    def get_name(self):
        return f'{self.__first} {self.__last}'

    def get_first(self):
        return self.__first

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

    def set_role(self, role):
        self.__role = role

    def get_role(self):
        return self.__role

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_shift(self, shift):
        self.__shift = shift

    def get_shift(self):
        return self.__shift

    def __str__(self):
        return f'''{self.get_name()}
        \r . ID: {self.get_id()}
        \r . Address: {self.get_address()}
        \r . Role: {self.get_role()}
        \r . Salary: {self.get_salary()}
        \r . Shift: {self.get_shift()}'''

    def __repr__(self):
        return f'Employee({self.get_name()}, {self.get_id()}, {self.get_address()}, {self.get_role()}, {self.get_salary()}, {self.get_shift()})'