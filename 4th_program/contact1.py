contacts = {}
while True:
    print("\n1.Add  2.Search  3.Delete  4.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        with open("contacts.txt", "w") as f:
            for n, p in contacts.items():
               f.write(n + " " + p + "\n")
        print("Contact Added")
    elif choice == 2:
        name = input("Enter name: ")
        print(contacts.get(name, "Contact Not Found"))
    elif choice == 3:
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted")
        else:
            print("Contact Not Found")
    else:
        break