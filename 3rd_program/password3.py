password = "admin123"
for i in range(3):
    p = input("Enter password: ")
    if p == password:
        print("Login Successful")
        break
    else:
        print("Wrong Password")
else:
    print("Account Locked")