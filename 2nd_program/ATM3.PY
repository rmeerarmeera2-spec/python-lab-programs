total = 0
while True:
    print("\n1. Pizza - Rs.200")
    print("2. Burger - Rs.100")
    print("3. Juice - Rs.50")
    print("4. View Bill")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        total = total + 200
        print("Pizza Added")
    elif choice == 2:
        total = total + 100
        print("Burger Added")
    elif choice == 3:
        total = total + 50
        print("Juice Added")
    elif choice == 4:
        print("Total Bill =", total)
    elif choice == 5:
        print("Thank You")
        break
    else:
        print("Invalid Choice")