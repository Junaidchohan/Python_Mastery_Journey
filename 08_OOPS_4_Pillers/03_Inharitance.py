# Class One and its called parent class
class Car:
    color = "Black"
    @staticmethod
    def Start():
        print("car start..")


    @staticmethod
    def Stop():
        print("car stop.")


# Class second and its called child class and here parent class we write in ()
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")

print(car1.name)
print(car1.Start) # Here we access our parent class Propertys/Attributes as (Start Method)
print(car1.color) # # Here we access our parent class Propertys/Attributes as (color property)

