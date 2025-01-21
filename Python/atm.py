
balance = 0

def atm():
   
    global balance
    while True:
        print("\nWelcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"Your balance is: ${balance}")
        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"${amount} deposited successfully. New balance is: ${balance}")
            else:
                print("Invalid amount")
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            if 0 < amount <= balance:
                balance -= amount
                print(f"${amount} withdrawn successfully. New balance is: ${balance}")
            else:
                print("Invalid amount or insufficient balance")
        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice")

atm()
