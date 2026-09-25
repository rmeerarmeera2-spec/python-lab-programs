expenses = {}
n = int(input("Number of expenses: "))
for i in range(n):
    item = input("Item: ")
    amount = int(input("Amount: "))
    expenses[item] = amount
print("Expenses:", expenses)
print("Total:", sum(expenses.values()))