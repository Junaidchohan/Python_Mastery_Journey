#....................................Before useing the property decorater.....................................
# class Students:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

#     def calcPercentage(self):
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"


# s1 = Students(89, 99, 81)
# print(s1.percentage)

# s1.phy = 86
# print(s1.phy)
# s1.calcPercentage()
# print(s1.percentage)


#.......................................After using property decorater....................................
class Students:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math


    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Students(89, 99, 81)
print(s1.percentage)

s1.phy = 86
print(s1.percentage)



