"""
Keywords are reserved words in Python.
You cannot use them as variable names, function names, or identifiers.
"""

# Import keyword module to see all Python keywords
import keyword

# Print all Python keywords
print("List of Python Keywords:")
print(keyword.kwlist)

print("\nTotal Keywords:", len(keyword.kwlist))


# Example: Using keywords correctly

# if, else, for, while are keywords
number = 10

if number > 5:
    print("Number is greater than 5")
else:
    print("Number is 5 or smaller")

