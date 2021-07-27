from datetime import datetime
import pytz

WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'
BLUE = '\033[1;36m'

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.balance += amount
        print(f'You deposit {amount} units')
        self.show_balance()
        self.history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'You spent {amount} units')
            self.history.append([-amount, self._get_current_time()])
        else:
            print(f'Not enough money')
        self.show_balance()

    def show_balance(self):
        print(f'Balance {self.balance} units')

    def show_history(self):
        for amount, date in self.history:
            if amount > 0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdrawn'
                color = RED
            print(f'{color} {amount} {WHITE} {transaction} on {date.astimezone().isoformat()}')
        print(f'{self.name}, ваш текущий баланс: {BLUE} {self.balance} {WHITE}')


        # print(f'Выписка: текущий баланс {self.balance}')
        # for i in range(len(self.history)):
        #     print(f'{self.history[i]}')

a = Account('Denis', 100)

a.deposit(223)
a.withdraw(135)
a.deposit(50)
a.withdraw(200)
a.show_history()