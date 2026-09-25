n = int(input("Enter number of students: "))
total = 0
for i in range(n):
    attendance = int(input("Enter attendance percentage: "))
    total = total + attendance
average = total / n
print("Total Attendance =", total)
print("Average Attendance =", average)
if average >= 90:
    status = "Excellent"
elif average >= 75:
    status = "Good"
elif average >= 60:
    status = "Average"
else:
    status = "Poor"
print("Attendance Status =", status)