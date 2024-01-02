import math

# Simple calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

# Additional functions
def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Cannot calculate square root of a negative number"

def percentage(x, y):
    return (x * y) / 100

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

# User input for numbers and operation
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, ^, sqrt, %, !): ")

if operator == "!":
    # Factorial only needs one number
    result = factorial(num1)
else:
    # Factorial does not need the second number
    num2 = float(input("Enter second number: "))
    
    # Perform calculation based on operator
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    elif operator == "^":
        result = power(num1, num2)
    elif operator == "sqrt":
        result = square_root(num1)
    elif operator == "%":
        result = percentage(num1, num2)
    else:
        result = "Error: Invalid operator"

# Display the result
print(f"Result: {result}")
