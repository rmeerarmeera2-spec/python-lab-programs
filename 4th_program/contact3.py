books = {}
while True:
    print("\n1.Add  2.Search  3.Delete  4.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        book = input("Book Name: ")
        author = input("Author: ")
        books[book] = author
        print("Book Added")
    elif ch == 2:
        book = input("Book Name: ")
        print(books.get(book, "Book Not Found"))
    elif ch == 3:
        book = input("Book Name: ")
        books.pop(book, None)
        print("Book Deleted")
    else:
        break