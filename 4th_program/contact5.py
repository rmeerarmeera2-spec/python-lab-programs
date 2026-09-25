employees = {}
n = int(input("Number of employees: "))
for i in range(n):
    name = input("Name: ")
    salary = int(input("Salary: "))
    employees[name] = salary
name = input("Search employee: ")
if name in employees:
    print("Salary:", employees[name])
else:
    print("Employee Not Found")