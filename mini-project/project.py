import sys


CORRECT_PIN = "1234"  
balance = 500.00  # Default balance

# Authentication the user
def authenticate():
    attempts = 3
    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")
        if pin == CORRECT_PIN:
            print("\nPIN accepted. Welcome to Humber Bank!\n")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts remaining: {attempts}\n")
    
    print("Too many incorrect attempts. Exiting program.")
    sys.exit()

# Function to display the balance
def check_balance():
    print(f"\nYour current balance is: ${balance:.2f}\n")

# Function to handle withdrawals
def withdraw():
    global balance  # Use the global balance variable

    print("\nWithdrawal Options:")
    print("1: $20  |  2: $40  |  3: $60  |  4: $80  |  5: $100  |  6: Custom Amount")

    while True:
        try:
            choice = int(input("Select an option (1-6): "))

            withdrawal_options = {1: 20, 2: 40, 3: 60, 4: 80, 5: 100}
            
            if choice in withdrawal_options:
                amount = withdrawal_options[choice]
            elif choice == 6:
                amount = float(input("Enter custom withdrawal amount: "))
            else:
                print("Invalid option. Please select a number from 1 to 6.")
                continue

            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")
                continue

            if amount > balance:
                print("Insufficient funds. Try a lower amount.")
                continue

            balance -= amount
            print(f"\nSuccessfully withdrew ${amount:.2f}")
            check_balance()
            break

        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to handle deposits
def deposit():
    global balance  

    while True:
        try:
            amount = float(input("\n💰 Enter deposit amount: "))

            if amount <= 0:
                print("Deposit amount must be greater than zero.")
                continue

            balance += amount
            print(f"\nSuccessfully deposited ${amount:.2f}")
            check_balance()
            break

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def banking_menu():
    while True:
        print("\n Humber Bank Menu")
        print("1: Check Balance")
        print("2: Withdraw Money")
        print("3: Deposit Money")
        print("4: Exit")

        try:
            choice = int(input("\nEnter your choice (1-4): "))

            if choice == 1:
                check_balance()
            elif choice == 2:
                withdraw()
            elif choice == 3:
                deposit()
            elif choice == 4:
                print("Thank you for using Humber Bank. Goodbye!")
                sys.exit()
            else:
                print("Invalid option. Please select a number from 1 to 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")

        # Ask if the user wants another transaction
        again = input("\nWould you like to perform another transaction? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using Humber Bank. Goodbye!")
            sys.exit()


print("\nWelcome to Humber Bank Terminal")
authenticate()  
