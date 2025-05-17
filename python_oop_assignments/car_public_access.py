class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

# Test
car1 = Car("Toyota")
print(car1.brand)
car1.start()
