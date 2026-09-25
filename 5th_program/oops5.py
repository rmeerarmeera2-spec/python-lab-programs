class Employee:
    def work(self):
        print("Employee Working")
class Manager(Employee):
    def work(self):
        print("working employees")
name = input("Enter name: ")
salary = int(input("Enter salary: "))
m = Manager()
m.work()
print("Name:", name)
print("Salary:", salary)