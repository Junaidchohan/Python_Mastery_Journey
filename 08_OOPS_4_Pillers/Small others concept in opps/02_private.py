

# ..........................Programm Number One .................................................................
# ............................................................................................................


class Account:
    def __init__(self, acc_no, acc_pass):
        self.account_no = acc_no    # Now its attributes is public and we can access via obj out of class
        self.acc_pass = acc_pass    # Now its attributes is public

acc1 = Account(12344, 11000)
print(acc1.account_no)
print(acc1.acc_pass)



class Account:
    def __init__(self, acc_no, acc_pass):
        self.account_no = acc_no   # Now its attributes is private and we cant access via obj out of class
        self.__balance = acc_pass  # Now its attributes is private its accessed in which class fun but not outside

    def reset_pass(self):
        print(self.__account_no)

acc1 = Account(12344, 11000)
print(acc1.account_no)
print(acc1.reset_pass)





# ..........................Programm Number Two .................................................................
# .......................................................................................................

class Person:
    __name = "Anonymous" # Private Attribute

    def __hello(self):   # Private Method its access in this class not out of this class because its private
        print("hello person")

    def wellcome(self):  # We can access hello method here bcz its Wellcome fun within a class
        self.__hello()

p1 = Person()

print(p1.wellcome())    # But Wellcome fun we can access out of this class because its Public method

