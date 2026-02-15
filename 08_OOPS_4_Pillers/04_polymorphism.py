# .....................................Oprater Overloading..............................................
# Its called polymorphism bcz + oprater work behaiver on the base of where we use this
# when the same oprater is allowed to have diff meaning according to the context
print(1+2) # here its work can add the value
print(type(1))
print("Junaid" + "Chohan") # here its work can concatinate the string
print(type("junaid"))
print([1, 2, 3] + [4, 5, 6]) # here its work merge the string
print(type([1, 2, 3]))


#........................For creating complex number sys without Dunder fun...............................

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")

#     def add(self, num2):
#         newReal = self.real + num2.real
#         newImg  = self.img  + num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(1, 3)
# num1.showNumber()

# num2 = Complex(4, 3)
# num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()


# ..........................................With Dunder fun...............................................
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):    # ...................Its called Dunder fun( __add__ )....................
        newReal = self.real + num2.real
        newImg  = self.img  + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):    # ...................Its called Dunder fun( __sub__ )....................
        newReal = self.real - num2.real
        newImg  = self.img  - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 3)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()