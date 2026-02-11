"""
Concept: Tokens in Python

Tokens are the smallest units in a Python program.

Types of Tokens:
1. Keywords
2. Identifiers
3. Literals
4. Operators
5. Punctuators (Separators)
"""

# ----------------------------
# 1. Keywords
# ----------------------------
import keyword
print("Keywords Example:")
print(keyword.kwlist[:5])   # printing first 5 keywords


# ----------------------------
# 2. Identifiers
# ----------------------------
student_name = "Junaid"
print("\nIdentifier Example:")
print(student_name)


# ----------------------------
# 3. Literals
# ----------------------------
age = 22           # Integer literal
price = 99.5       # Float literal
name = "Ali"       # String literal
is_active = True   # Boolean literal

print("\nLiterals Example:")
print(age, price, name, is_active)


# ----------------------------
# 4. Operators
# ----------------------------
a = 10
b = 5
print("\nOperators Example:")
print("Addition:", a + b)
print("Multiplication:", a * b)


# ----------------------------
# 5. Punctuators (Separators)
# ----------------------------
# Examples: ( ) { } [ ] , : ; . @ =
numbers = [1, 2, 3]   # [] brackets
print("\nPunctuators Example:")
print(numbers)


# ===================================================
# Type Conversion
# ===================================================

print("\nType Conversion")

# ----------------------------
# Implicit Type Conversion
# ----------------------------
# Python automatically converts smaller type to larger type

x = 5        # int
y = 2.5      # float

result = x + y   # int automatically converted to float
print("\nImplicit Conversion:")
print("Result:", result)
print("Type of result:", type(result))


# ----------------------------
# Explicit Type Conversion (Type Casting)
# ----------------------------
# User manually converts type

num = "100"

converted_num = int(num)   # converting string to int

print("\nExplicit Conversion:")
print("Converted Value:", converted_num)
print("Type:", type(converted_num))
