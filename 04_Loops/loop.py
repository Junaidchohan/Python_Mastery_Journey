"""
Loops in Python

Loops are used to execute a block of code multiple times.

Types:
1. for loop
2. while loop
3. Nested loops
4. Loop control statements (break, continue, pass)
"""

# ---------------------------------
# 1. for Loop
# ---------------------------------

print("For loop example:")

for i in range(5):
    print("Value of i:", i)


# ---------------------------------
# 2. for Loop with List
# ---------------------------------

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print("Fruit:", fruit)


# ---------------------------------
# 3. while Loop
# ---------------------------------

print("\nWhile loop example:")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# ---------------------------------
# 4. break Statement
# ---------------------------------

print("\nBreak example:")

for num in range(10):
    if num == 5:
        break
    print(num)


# ---------------------------------
# 5. continue Statement
# ---------------------------------

print("\nContinue example:")

for num in range(5):
    if num == 2:
        continue
    print(num)


# ---------------------------------
# 6. pass Statement
# ---------------------------------

print("\nPass example:")

for i in range(3):
    pass   # Placeholder, does nothing

print("Loop completed using pass.")


# ---------------------------------
# 7. Nested Loop
# ---------------------------------

print("\nNested loop example:")

for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)
