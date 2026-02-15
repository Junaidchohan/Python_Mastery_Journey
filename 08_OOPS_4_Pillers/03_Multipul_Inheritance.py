class A:
    varA = "Wellcome to class A"
class B:
    varB = "Wellcome to class B"

class C(A, B): # Multipul Inheritance Here we can Inherit two classes in C class
    varC = "Wellcome to class C"

c1 = C()

print(c1.varC)
print(c1.varA)
print(c1.varB)
