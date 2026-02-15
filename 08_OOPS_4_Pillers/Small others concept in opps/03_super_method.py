class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def Start():
        print("car start..")


    @staticmethod
    def Stop():
        print("car stop.")


class ToyotaCar(Car):
    def __init__(self, name, type):
       # If we need here to access the type attribute/Method of parent class constructor,
       # (in simple word we need to acces the constracter property of the parent class and for this purpose we use Super method)
       # We use Super Method to call Constructor of otheres class
       super().__init__(type)
       super().Start() # As Welll we can access the methods of otheres classes
       self.name = name



car1 = ToyotaCar("fortuner", "electric")

print(car1.name)
print(car1.type)


