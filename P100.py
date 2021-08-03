import shutil
import random

class ATMmachine:
    def __init__(self, cardNumber, pin, balance = 10000):
        self.cardNumber = cardNumber
        self.pin = pin
        self.balance = random.randint(1, 1000000)
    
    def checkBalance(self):

        print("Your Current Balance is: $", self.balance)

    def withdraw(self, withdrawal_amount):
        self.balance = self.balance - withdrawal_amount
        print("You have successfully withdrawn $" + str(withdrawal_amount))
        print("Your current balance is now: $", self.balance)

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print("You have successfully deposited $" + str(deposit_amount))
        print("Your current balance is now: $", self.balance)


def main():
    columns = shutil.get_terminal_size().columns
    print("Welcome To Generic Bank ATM".center(columns))
    card_number = input("Enter your card number: ")
    pin_number = input("Enter your PIN: ")
    new_user = ATMmachine(card_number, pin_number)

    print("Choose an activity".center(columns))
    print("1.Balance, 2.Withdraw, 3.Deposit".center(columns))
    activity = int(input("Enter Activity Number: "))
    if (activity == 1):
        new_user.checkBalance()

    if (activity == 2):
        amount = int(input("Enter amount to withdraw: "))
        new_user.withdraw(amount)

    if (activity == 3):
        amount = int(input("Enter amount to deposit: "))
        new_user.deposit(amount)

if __name__ == "__main__":
    main()
