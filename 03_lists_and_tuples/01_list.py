marks = [12, 13, 14, 15, 16, 17]
print(marks)
print(type(marks))


# we can store in list multipul types of values
data = [12, "junaid", 14, 15, 16, 17]
print(data)

# Sclicing in python like in strings
data = [12, "junaid", 14, 15, 16, 17]
print(data[2:])

# List Methods
list = [4, 3, 5]
print(list)


# 01 Append
list = [4, 3, 5]
print(list)
print(list.append(6)) #print this line is none because values update on next line
print(list)


# 02 sort
list = [4, 3, 5]
print(list.sort()) # sort in accending order
print(list)

# 03 sort reverse
list = [4, 3, 5]
print(list.sort(reverse= True)) # sort in decending order
print(list)


# 04 reverse
list = [4, 3, 5]
print(list.reverse())
print(list)

# 05 insert
list = [4, 3, 5]
list.insert(1,8)
print(list)


# 06 remove
list = [4, 3, 5]
list.remove(3)
print(list)

# 07 pop
list = [4, 3, 5]
list.pop(2)
print(list)

