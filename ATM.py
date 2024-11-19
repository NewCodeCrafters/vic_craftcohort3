# This console app stimulate an ATM machine
# It does the following - 1. Display current balance 2. Allows cash deposit 3. Allows cash withdrawal


class ATM:
    def __init__(self, balance = 0):
        self.balance = balance

    def display_balance(self):
        print(f"Your current balance is NGN{self.balance}")

    def deposit(self, amount):
        self.balance = self.balance+ amount
        print(f"{amount} has been deposited")
        self.display_balance()

    def withdrawal(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds . Dear customer, please fund your account")
        else:
            self.balance = self.balance - amount
            self.display_balance()

def main():
    machine1 = ATM(30000)

    while True:
        print(f"Welcome to our bank. How can we help you dear customer!")
        print(f"\n1. Check balance")
        print(f"2. Cash deposit")
        print(f"3. withdraw")
        print("4. Exit")
        choice = input("Enter your choice here [1-4]:  ")

        if choice == '1':
            machine1.display_balance()
        elif choice == '2' :
            amount = float (input("Enter an amount to withdraw:   "))
            machine1.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter an amount:  "))
            machine1.withdrawal(amount)
        elif choice == '4':
            break
        else:
            print("Invalid entry!!!, Please try again")
            continue
main()