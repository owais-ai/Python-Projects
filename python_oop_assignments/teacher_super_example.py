class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Test
t1 = Teacher("Sara", "Math")
print(t1.name, t1.subject)
