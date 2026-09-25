n = int(input("Enter number of days: "))
total = 0
for i in range(n):
    temp = int(input("Enter temperature: "))
    total = total + temp
average = total / n
print("Total Temperature =", total)
print("Average Temperature =", average)
if average >= 35:
    print("Temperature = Hot")
elif average >= 25:
    print("Temperature = Warm")
elif average >= 15:
    print("Temperature = Cool")
else:
    print("Temperature = Cold")