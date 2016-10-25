class BankAccount(object):
    balance = 0

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "%s's account. Balance: $%.2f" % (self.name, self.balance)

    def show_balance(self):
        return "%.2f" % (self.balance)

    def deposit(self, amount):
        if amount < 0:
            print "Invalid value"
            return
        else:
            print "Amount %.2f deposited" % (amount)
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print "Insufficent balance"
            return
        else:
            print "Amount %.2f withdraw" % (amount)
            self.balance -= amount
            self.show_balance()


my_account = BankAccount("Jhon")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account
