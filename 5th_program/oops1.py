class User:
    def action(self):
        print("User can borrow a book")
class Student(User):
    def action(self):
        print("Student borrowed a book")
class Book:
    def __init__(self, name):
        self.name = name
        self.available = True
    def issue(self):
        if self.available:
            self.available = False
            print(self.name, "Issued")
        else:
            print("Book Not Available")
    def return_book(self):
        self.available = True
        print(self.name, "Returned")
book = Book("Python Programming")
user = Student()
user.action()          
book.issue()
book.return_book()