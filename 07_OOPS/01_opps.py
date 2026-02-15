# # Ex01
# class Students:
#     name = "Junaid"

# s1 = Students()
# print(s1.name)

# s2 = Students()
# print(s2.name)

# # Ex02
# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color, car1.brand)



# Constractor in python
class Students:
    college_name = "SSPI" # Attributes of class its create one time in class, but name & marks create 2 time even as much we create the obj and as much auto create the name and marks
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new students in database")
    #  Methods in python
    def wellcome(self):
        print("Wellcome Students")

s1 = Students("junaid", 98)
print(s1.name, s1.marks)

s2 = Students("Umair", 98)
print(s2.name, s2.marks)

print(Students.college_name)
s2.wellcome()