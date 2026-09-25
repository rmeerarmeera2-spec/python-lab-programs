n = int(input("Enter number of products: "))
total = 0
for i in range(n):
    sales = int(input("Enter sales amount: "))
    total = total + sales
average = total / n
print("Total Sales =", total)
print("Average Sales =", average)
if average >= 50000:
    print("Performance = Excellent")
elif average >= 25000:
    print("Performance = Good")
elif average >= 10000:
    print("Performance = Average")
else:
    print("Performance = Poor")