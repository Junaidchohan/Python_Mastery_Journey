"""
Functions in Python

A function is a reusable block of code
that performs a specific task.

Syntax:
def function_name(parameters):
    code
    return value
"""

# ---------------------------------
# 1. Simple Function
# ---------------------------------

def greet():
    print("Hello, welcome to Python.")

greet()


# ---------------------------------
# 2. Function with Parameters
# ---------------------------------

def greet_user(name):
    print("Hello", name)

greet_user("Junaid")


# ---------------------------------
# 3. Function with Return Value
# ---------------------------------

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)


# ---------------------------------
# 4. Default Parameters
# ---------------------------------

def power(base, exponent=2):
    return base ** exponent

print("Square:", power(4))
print("Cube:", power(4, 3))


# ---------------------------------
# 5. Keyword Arguments
# ---------------------------------

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=22, name="Ali")


# ---------------------------------
# 6. Arbitrary Arguments (*args)
# ---------------------------------

def total_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("Total:", total_sum(1, 2, 3, 4))


# ---------------------------------
# 7. Function Inside Function
# ---------------------------------

def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()
