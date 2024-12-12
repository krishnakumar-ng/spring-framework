
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self):
        print("Account Ctor......")

    def deposit(self):
        pass

    @abstractmethod
    def checkBalance(self):
        pass

class Savings(Account):

    def withdraw(self):
        print("debited.....")

    def checkBalance(self):
        print('Balance in the account is ######.##')

sav = Savings()
sav.withdraw()
sav.checkBalance()