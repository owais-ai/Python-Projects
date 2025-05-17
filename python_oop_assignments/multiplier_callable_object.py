class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, num):
        return self.factor * num

# Test
m = Multiplier(3)
print(callable(m))
print(m(10))
