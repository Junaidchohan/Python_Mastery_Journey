"""
Expression:
An expression is a combination of values, variables, and operators
that produces a result.

Execution:
Execution means Python reads and runs the code line by line from top to bottom.
"""

# -----------------------------
# 1. Simple Arithmetic Expression
# -----------------------------

a = 10
b = 5

result = a + b   # This is an expression

print("Addition Result:", result)


# -----------------------------
# 2. Expression with Multiple Operators
# -----------------------------

value = 10 + 5 * 2   # Multiplication runs first

print("Expression 10 + 5 * 2 =", value)


# -----------------------------
# 3. Using Parentheses (Order Control)
# -----------------------------

value2 = (10 + 5) * 2   # Parentheses run first

print("Expression (10 + 5) * 2 =", value2)


# -----------------------------
# 4. Comparison Expression
# -----------------------------

x = 20
y = 15

comparison = x > y   # This expression returns True or False

print("Is x greater than y?", comparison)


# -----------------------------
# 5. Logical Expression
# -----------------------------

age = 22
has_id = True

allowed = age >= 18 and has_id

print("Is person allowed?", allowed)


# -----------------------------
# Execution Example
# -----------------------------

print("\nExecution Flow Example:")

number = 5
print("Step 1: number =", number)

number = number + 3   # Python evaluates right side first
print("Step 2: number =", number)

number = number * 2
print("Step 3: number =", number)

print("Execution finished.")
