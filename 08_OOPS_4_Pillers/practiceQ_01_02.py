class Account:
    def __init__(self, acc, bal):
        self.account_no = acc
        self.balance = bal

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance = ", self.get_balance())



    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance = ", self.get_balance())


    def get_balance(self):
        return self.balance

acc1 = Account(12345, 10000)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(50000) # My salary add
acc1.debit(9500)    # Rent pay








