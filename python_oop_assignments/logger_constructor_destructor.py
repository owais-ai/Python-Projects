class Logger:
    def __init__(self):
        print("Logger created!")

    def __del__(self):
        print("Logger destroyed!")

# Test
log = Logger()
del log
