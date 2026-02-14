"""
Recursion in Python

Recursion is when a function calls itself.

Important:
Every recursive function must have a base case.
Without a base case, it will cause infinite recursion.
"""

# ---------------------------------
# 1. Simple Countdown Example
# ---------------------------------

def countdown(n):
    if n == 0:          # Base case
        print("Finished")
        return
    print(n)
    countdown(n - 1)    # Recursive call

countdown(5)


# ---------------------------------
# 2. Factorial Using Recursion
# ---------------------------------

def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# ---------------------------------
# 3. Sum of Natural Numbers
# ---------------------------------

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print("Sum of first 5 numbers:", sum_n(5))


# ---------------------------------
# 4. Fibonacci Series
# ---------------------------------

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci at position 6:", fibonacci(6))
