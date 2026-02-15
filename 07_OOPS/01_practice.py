class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for val  in self.marks:
               sum += val
        print("Hi", self.name, "your avg score is:", sum/3)

s1 = Students("junaid", [98, 97, 96])
s1.avg()
