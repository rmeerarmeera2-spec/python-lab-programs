books = 5
while True:
    print("\n1. View Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Available Books =", books)
    elif choice == 2:
        if books > 0:
            books = books - 1
            print("Book Issued")
        else:
            print("No Books Available")
    elif choice == 3:
        books = books + 1
        print("Book Returned")
    elif choice == 4:
        print("Thank You")
        break
    else:
        print("Invalid Choice")