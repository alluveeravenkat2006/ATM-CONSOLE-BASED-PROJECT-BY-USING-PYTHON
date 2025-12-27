#
# MINI PROJECT – ATM MANAGEMENT SYSTEM USING OOPS

#  Abstraction
from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def transaction(self):
        pass   # abstract method

#  BASE CLASS


class Account(BankAccount):

    bank_name = "ABC Bank"   # class variable

    def __init__(self, name, acc_num, balance, pin):
        self.name = name                # public
        self._acc_num = acc_num         # protected
        self.__balance = balance        # private
        self.__pin = pin                # private
        self.history = []               # transaction history


    def get_balance(self):
        return self.__balance


    def set_balance(self, amount):
        self.__balance = amount

    # PIN verification
    def verify_pin(self, pin):
        return pin == self.__pin


    def transaction(self):
        pass



#  CHILD CLASS


class ATM(Account):

    # Class Method
    @classmethod
    def show_bank_name(cls):
        print(f"\nWELCOME TO {cls.bank_name.upper()} ATM\n")

    # Static Method
    @staticmethod
    def validate_amount(amount):
        return amount > 0


    def transaction(self):
        print("Transaction started...")

    # Instance Methods
    def check_balance(self):
        print(f"\nAvailable Balance: ₹{self.get_balance()}")

    def deposit(self, amount):
        if not ATM.validate_amount(amount):
            print("\nInvalid amount! Deposit value must be greater than 0.")
            return

        new_bal = self.get_balance() + amount
        self.set_balance(new_bal)
        self.history.append(f"Deposited ₹{amount}")

        print("\nDeposit successful!")
        print(f"Updated Balance: ₹{new_bal}")

    def withdraw(self, amount):
        if not ATM.validate_amount(amount):
            print("\nInvalid amount! Withdrawal value must be greater than 0.")
            return

        if amount > self.get_balance():
            print("\nInsufficient balance!")
            return


        if amount > 20000:
            print("\nMaximum withdrawal limit is ₹2000!")
            return

        new_bal = self.get_balance() - amount
        self.set_balance(new_bal)
        self.history.append(f"Withdrawn ₹{amount}")

        print("\nWithdrawal successful!")
        print(f"Updated Balance: ₹{new_bal}")

    def account_details(self):
        print("\n----- ACCOUNT DETAILS -----")
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self._acc_num}")
        print(f"Balance: ₹{self.get_balance()}")
        print("-----------------------------")

    def show_history(self):
        print("\n----- TRANSACTION HISTORY -----")
        if len(self.history) == 0:
            print("No transactions done yet.")
        else:
            for item in self.history:
                print(item)
        print("-------------------------------")



#  MAIN PROGRAM


# Create an ATM user object
ATM.show_bank_name()
user = ATM("A V V SATYANARAYANA", 230104, 1000, pin=230104)

print("Please insert your card...\n")

# PIN verification system
for attempt in range(3):
    upin = int(input("Enter ATM PIN: "))
    if user.verify_pin(upin):
        print("\nLogin Successful!\n")
        break
    else:
        print("Wrong PIN!")
else:
    print("\nToo many wrong attempts! Card blocked.")
    exit()

# Menu Loop
while True:
    print("""
-----------------------------
ATM MENU
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Account Details
5. Transaction History
6. Exit
-----------------------------
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        user.check_balance()

    elif choice == "2":
        amt = int(input("Enter amount to deposit: "))
        user.deposit(amt)

    elif choice == "3":
        amt = int(input("Enter amount to withdraw: "))
        user.withdraw(amt)

    elif choice == "4":
        user.account_details()

    elif choice == "5":
        user.show_history()

    elif choice == "6":
        print("\nThank you for using the ATM. Please take your card.")
        break

    else:
        print("\nInvalid choice! Please try again.")
