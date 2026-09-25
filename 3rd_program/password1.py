password = input("Enter password: ")
if len(password) >= 8:
    encrypted = ""
    for ch in password:
        encrypted += chr(ord(ch) + 3)
    print("Password is Strong")
    print("Encrypted Password:", encrypted)
    with open("password.txt", "w") as f:
        f.write(encrypted)
    print("Saved successfully!")
else:
    print("Password is Weak")
    print("Use at least 8 characters.")