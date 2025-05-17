class Employee:
    def __init__(self):
        self.name = "Ali"       # Public
        self._salary = 50000    # Protected
        self.__ssn = "123-45"   # Private

emp = Employee()
print(emp.name)       # OK
print(emp._salary)    # OK but not recommended
# print(emp.__ssn)    # Error
print(emp._Employee__ssn)  # Access via name mangling
