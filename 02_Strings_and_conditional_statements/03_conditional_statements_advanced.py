"""
Concept: Conditional Statements in Python

Conditional statements allow the program to make decisions
based on conditions that return True or False.
"""

# ---------------------------------
# 1. Simple if
# ---------------------------------

number = 10

if number > 5:
    print("Number is greater than 5")


# ---------------------------------
# 2. if-else
# ---------------------------------

age = 16

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


# ---------------------------------
# 3. if-elif-else (Multiple Conditions)
# ---------------------------------

marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# ---------------------------------
# 4. Nested if
# ---------------------------------

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
    else:
        print("ID required")
else:
    print("Underage")


# ---------------------------------
# 5. Using Logical Operators
# ---------------------------------

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid login")


# ---------------------------------
# 6. Using 'not' Operator
# ---------------------------------

is_logged_in = False

if not is_logged_in:
    print("Please log in first")


# ---------------------------------
# 7. Short Hand if (One Line)
# ---------------------------------

x = 5
if x > 0: print("Positive number")


# ---------------------------------
# 8. Ternary Conditional Operator
# ---------------------------------

num = 7
result = "Even" if num % 2 == 0 else "Odd"

print("Number is", result)
