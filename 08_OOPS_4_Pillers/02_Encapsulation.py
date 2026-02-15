# Wrraping data and fun into single unit(Object)
# In simple words we make a capsule (Data+Fun) its called Encapsulation
# Basically we make a class which one have (Attribute+Method) and we use via Object

class Car:
    def __init__(self):
        self.acc = False #Attributes
        self.brk = False
        self.clutch = False

    def Start(self):    #Methods
        self.acc = True
        self.clutch = True
        print("Car is Start Now")

car1 = Car()
car1.Start()