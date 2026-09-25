data = input("Enter data: ")
encrypted = ""
for ch in data:
    encrypted += chr(ord(ch) + 3)
with open("data.txt", "w") as f:
    f.write(encrypted)
print("Data Encrypted and Saved")