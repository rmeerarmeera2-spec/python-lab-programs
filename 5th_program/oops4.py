class Product:
    def show(self):
        print("Product")
class Mobile(Product):
    def show(self):
        print("Product details")
name = input("Enter product: ")
price = int(input("Enter price: "))
p = Mobile()
p.show()
print("Product:", name)
print("Price:", price)