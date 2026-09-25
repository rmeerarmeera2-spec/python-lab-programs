n = int(input("Enter number of customers: "))
total = 0
for i in range(n):
    units = int(input("Enter units consumed: "))
    total = total + units
average = total / n
print("Total Units =", total)
print("Average Units =", average)

if average >= 500:
    print("Category = High Consumption")
elif average >= 200:
    print("Category = Medium Consumption")
else:
    print("Category = Low Consumption")