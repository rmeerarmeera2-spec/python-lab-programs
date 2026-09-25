tickets = 20
while True:
    print("\n1. View Tickets")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Available Tickets =", tickets)
    elif choice == 2:
        n = int(input("Enter number of tickets: "))
        if n <= tickets:
            tickets = tickets - n
            print("Tickets Booked")
        else:
            print("Tickets Not Available")
    elif choice == 3:
        n = int(input("Enter number of tickets to cancel: "))
        tickets = tickets + n
        print("Tickets Cancelled")
    elif choice == 4:
        print("Thank You")
        break
    else:
        print("Invalid Choice")