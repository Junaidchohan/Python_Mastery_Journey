# Hiding the implementaion details of class and showing the essential features to user.
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def Start(self):    # these all steps hide its in class Like "self.acc = True" and "self.clutch = True"
        self.acc = True # Unnessesry details is hide
        self.clutch = True
        print("Car is Start Now")

car1 = Car() # We show to user just car is start now.
car1.Start() #