"""
Strings in Python

A string is a sequence of characters.
Strings are immutable. That means they cannot be changed after creation.
"""

# ---------------------------------
# 1. Creating Strings
# ---------------------------------

name = "Junaid"
message = 'Hello World'

print(name)
print(message)


# ---------------------------------
# 2. String Indexing
# ---------------------------------
# Index starts from 0

word = "Python"

print("First character:", word[0])
print("Second character:", word[1])
print("Last character:", word[-1])


# ---------------------------------
# 3. String Slicing
# ---------------------------------
# Format: string[start:end]

text = "Programming"

print("Slice 0 to 6:", text[0:6])
print("Slice 3 to 8:", text[3:8])
print("From start to 5:", text[:5])
print("From 5 to end:", text[5:])
print("Reverse string:", text[::-1])


# ---------------------------------
# 4. String Length
# ---------------------------------

print("Length of text:", len(text))


# ---------------------------------
# 5. Common String Functions
# ---------------------------------

sentence = "python is powerful"

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Capitalize:", sentence.capitalize())
print("Title Case:", sentence.title())

print("Replace word:", sentence.replace("powerful", "easy"))

print("Count 'o':", sentence.count("o"))

print("Find 'is':", sentence.find("is"))

print("Starts with python:", sentence.startswith("python"))
print("Ends with powerful:", sentence.endswith("powerful"))


# ---------------------------------
# 6. String Concatenation
# ---------------------------------

first = "Hello"
second = "World"

result = first + " " + second
print("Concatenation:", result)


# ---------------------------------
# 7. f-String Formatting
# ---------------------------------

age = 22
info = f"My name is {name} and I am {age} years old."
print(info)
