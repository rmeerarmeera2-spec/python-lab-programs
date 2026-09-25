total = 0
while True:
    print("\n1. Add Product")
    print("2. View Total")
    print("3. Remove Amount")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        price = int(input("Enter product price: "))
        total = total + price
        print("Product Added")
    elif choice == 2:
        print("Total Amount =", total)

    elif choice == 3:
        price = int(input("Enter amount to remove: "))
        if price <= total:
            total = total - price
            print("Amount Removed")
        else:
            print("Invalid Amount")
    elif choice == 4:
        print("Thank You")
        break
    else:
        print("Invalid Choice")