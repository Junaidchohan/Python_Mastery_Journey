# Class One and its called parent class
class Car:
    @staticmethod
    def Start():
        print("car start..")


    @staticmethod
    def Stop():
        print("car stop.")


# Class second and its called child class of Car and parent class of Fortuner
class ToyotaCar(Car):
    def __init__(self, brand):
        self.name = brand


# Class thired and its called child class of ToyotaCar and its inherit the all property & Method of Car & ToyotaCar
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type




car1 = Fortuner("deisel")

print(car1.Start) # Here we access our parent class Propertys/Attributes as (Start Method)
print(car1.type) # # Here we access our parent class Propertys/Attributes as (color property)

