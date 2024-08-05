#!/usr/bin/python3


# bank_account.py

class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposit successful. New balance: ${self.account_balance:.2f}")

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrawal successful. New balance: ${self.account_balance:.2f}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")
