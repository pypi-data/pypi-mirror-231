# module_file.py

# Define a simple function
def greet(name):
    return f"Hello, {name}!"

# Define a class
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Define a global variable
PI = 3.141592653589793
