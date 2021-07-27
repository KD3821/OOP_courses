

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'You deposit {amount} units')
        self.show_balance()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'You spent {amount} units')
        else:
            print(f'Not enough money')
        self.show_balance()

    def show_balance(self):
        print(f'Balance {self.balance} units')


a = Account('Denis', 100)