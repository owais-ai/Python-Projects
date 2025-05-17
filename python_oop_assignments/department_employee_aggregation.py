class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

class Employee:
    def __init__(self, name):
        self.name = name

# Test
emp = Employee("Ali")
dept = Department("HR", emp)
print(dept.employee.name)
