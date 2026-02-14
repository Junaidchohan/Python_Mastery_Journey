"""
File Input and Output in Python

File handling allows us to:
- Read data from files
- Write data to files
- Append data to files

Modes:
'r'  -> Read
'w'  -> Write (overwrite)
'a'  -> Append
'x'  -> Create file
"""

# ---------------------------------
# 1. Writing to a File
# ---------------------------------

file = open("example.txt", "w")
file.write("Hello, this is Python file handling.\n")
file.write("This file was created using write mode.")
file.close()

print("Data written to file.")


# ---------------------------------
# 2. Reading from a File
# ---------------------------------

file = open("example.txt", "r")
content = file.read()
print("\nFile Content:")
print(content)
file.close()


# ---------------------------------
# 3. Appending to a File
# ---------------------------------

file = open("example.txt", "a")
file.write("\nThis line is added using append mode.")
file.close()

print("\nData appended successfully.")


# ---------------------------------
# 4. Using with Statement (Best Practice)
# ---------------------------------

with open("example.txt", "r") as file:
    data = file.read()
    print("\nReading using with statement:")
    print(data)


# ---------------------------------
# 5. Reading Line by Line
# ---------------------------------

with open("example.txt", "r") as file:
    print("\nReading line by line:")
    for line in file:
        print(line.strip())
