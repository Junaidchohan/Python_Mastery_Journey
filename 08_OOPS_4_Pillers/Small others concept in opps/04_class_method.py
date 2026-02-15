class Person:
    name = "Junaid"
    # Instance Method
    # def __init__(self, name):
    #     self.name = name

    # Static Method
    @staticmethod
    def hello():
        print("Hello")


    # Class Method
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("chohan")
print(p1.name)
print(Person.name)


