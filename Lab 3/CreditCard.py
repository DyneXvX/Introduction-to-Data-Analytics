#%%
from math import *
from random import randint


class CreditCard:

    CreditCards = {'1': 'Visa', '2': 'Mastercard', '3': 'Amex',
                   '4': 'Discover', '5': 'Not Supported Card Type'}

    def __init__(self, cardnum, cardOwner, exp):
        self.cardnum = cardnum
        self.cardOwner = cardOwner
        self.exp = exp
        self.limit = 1000
        self.balance = randint(0, 1000)

    def get_cardType(self):
        if (self.cardnum[5] == '1'):
            return CreditCard.CreditCards['1']
        elif(self.cardnum[5] == '2'):
            return CreditCard.CreditCards['2']
        elif(self.cardnum[5] == '3'):
            return CreditCard.CreditCards['3']
        elif(self.cardnum[5] == '4'):
            return CreditCard.CreditCards['4']
        else:
            return CreditCard.CreditCards['5']

    def processOrder(self, price):
        checkCard = self.get_cardType()
        if (checkCard == 'Not Supported Card Type'):
            return False
        elif (int(price) <= self.balance):
            self.balance = (price + self.balance)
            return True
        else:
            return False

    def get_cardOwner(self):
        return self.cardOwner

    def __str__(self):
        return f"{self.cardOwner} is the owner of the credit card with number {self.cardnum} which expires on {self.exp}. "
# %%
