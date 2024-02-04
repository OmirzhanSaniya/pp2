class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 0
        else:
            self.balance -= amount
            return self.balance    

owner = input()
balance = int(input())
acc = Account(owner, balance)

deposit_amount = int(input())
print(acc.deposit(deposit_amount))

withdraw_amount = int(input())
print(acc.withdraw(withdraw_amount))