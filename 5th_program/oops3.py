class Student:
    def display(self):
        print("Student Details")
class CollegeStudent(Student):
    def display(self):
        print("College Student")
name = input("Enter name: ")
mark = int(input("Enter mark: "))
s = CollegeStudent()
s.display()
print("Name:", name)
print("Mark:", mark)