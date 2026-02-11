"""
Identifiers are names given to:
- Variables
- Functions
- Classes
- Objects

Rules:
1. Must start with a letter (a-z, A-Z) or underscore (_)
2. Cannot start with a number
3. Can contain letters, numbers, and underscores
4. Cannot use Python keywords
5. Case-sensitive
"""

# Valid Identifiers
name = "Junaid"
_age = 22
student1 = "Ali"
total_marks = 90

print(name)
print(_age)
print(student1)
print(total_marks)


# Invalid Identifiers

# 1name = "Ali"        # Cannot start with number
# total-marks = 100    # Hyphen not allowed
# class = 5            # Cannot use keyword
# my name = "Test"     # Space not allowed


# Case Sensitivity Example
value = 10
Value = 20

print("value =", value)
print("Value =", Value)
