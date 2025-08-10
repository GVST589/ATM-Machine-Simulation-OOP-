class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"✅ Withdrawn ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("❌ Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.balance}")

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, name, balance)
            print(f"🎉 Account created for {name} with A/C No: {account_number}")
        else:
            print("❌ Account number already exists.")

    def access_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("❌ Account not found.")
            return None
        
#====================
# Main Program
#====================

if __name__ == "__main__":
    atm = ATM()

    while True:
        print("\n===== ATM MENU =====")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            acc_no = input("Enter Account Number: ")
            name = input("Enter Name: ")
            bal = float(input("Enter Initial Balance: "))
            atm.create_account(acc_no, name, bal)

        elif choice == "2":
            acc_no = input("Enter Account Number: ")
            account = atm.access_account(acc_no)
            if account:
                while True:
                    print("\n--- Account Menu ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Exit to Main Menu")
                    sub_choice = input("Enter choice: ")

                    if sub_choice == "1":
                        amt = float(input("Enter deposit amount: "))
                        account.deposit(amt)

                    elif sub_choice == "2":
                        amt = float(input("Enter withdraw amount: "))
                        account.withdraw(amt)

                    elif sub_choice == "3":
                        account.check_balance()

                    elif sub_choice == "4":
                        break

                    else:
                        print("❌ Invalid choice.")

        elif choice == "3":
            print("👋 Thank you for using our ATM!")
            break

        else:
            print("❌ Invalid choice.")
