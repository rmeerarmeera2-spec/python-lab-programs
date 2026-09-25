n = int(input("Enter number of employees: "))
total = 0
for i in range(n):
    salary = int(input("Enter salary: "))
    total = total + salary

average = total / n
print("Total Salary =", total)
print("Average Salary =", average)

if average >= 50000:
    print("Salary Level = High")
elif average >= 25000:
    print("Salary Level = Medium")
else:
    print("Salary Level = Low")