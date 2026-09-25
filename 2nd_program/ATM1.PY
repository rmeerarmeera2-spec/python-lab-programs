balance = 5000
while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Balance =", balance)
    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("Amount Deposited")
    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Amount Withdrawn")
        else:
            print("Insufficient Balance")
    elif choice == 4:
        print("Thank You")
        break
    else:
        print("Invalid Choice")