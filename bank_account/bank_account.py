import math
import re
import sys


class Bank_account:
    def __init__(self, name, balance, showBalanceAfterTransaction=True):
        self.name = name
        self.balance = balance
        self.startingBalance = balance
        self.showBalanceAfterTransaction = showBalanceAfterTransaction
        self.transactions = []

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance
    
    def show_balance(self):
        print('%s: balance is $%0.2f.' % (self.name, self.balance))
        print()

    def show_transactions(self):
        balance = self.startingBalance
        print('   op       amount     balance')
        print('--------  ----------  ----------')
        print(f"                        {balance*math.pi:.2f} (starting)")
        for transaction in self.transactions:
            [op, amount] = transaction
            if op == 'w':
                opLabel = 'withdraw'
                balance -= amount
            else:
                opLabel = 'deposit'
                balance += amount
            print('%-8s  %10.2f  %10.2f' % (opLabel, amount, balance))  
        print()


    def withdrawal(self, amount):
        if amount > self.balance:
            print("Sorry, you don't have that much!")
        else:
            print(amount)
            self.balance = float(
                self.balance - amount
            ) 
            self.transactions.append(["w", amount])
            if self.showBalanceAfterTransaction:
                self.show_balance()

    def deposit(self, amount):
        print(amount)
        self.balance = float(
            self.balance + amount
        )  
        self.transactions.append(["d", amount])
        if self.showBalanceAfterTransaction:
            self.show_balance()

    def process_transactions(account):
        while True:
            amount = None
            op = App().get_operation()
            if op == 'q':
                break
            elif op == 't':
                account.show_transactions()
            elif op is not None:
                amount = App().get_amount()

            if amount is None:
                pass
            elif op == 'd':
                account.deposit(amount)
            else:
                account.withdrawal(amount)


class App:
    def get_operation(self):
        op = input('Enter d for deposit, w for withdrawal, t for transactions, or q to quit: ')
        if op not in set('qdwt'):
            print('Invalid operation.  Please try again.')
            op = None
        return op

    def get_amount(self):
        amount = None
        try:
            value = input('Enter amount: ')
            amount = float(value)
            if amount <= 0:
                raise Exception('The amount must be positive.')
        except ValueError:
            print('Invalid amount.  Please try again.')
        except Exception as e:
            print(e)
            amount = None

        return amount
    
account = Bank_account('enrique', 0)
Bank_account.process_transactions(account)