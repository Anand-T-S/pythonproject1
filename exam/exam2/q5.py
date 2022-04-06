# method overriding:same method name and same number of arguments
#The child class overrides parent class

class Book:
    def selectBook(self):
        print("B1")
class Child(Book):
    def selectBook(self):
        print("B2")
class Children(Child):
    def selectBook(self):
        print("B3")
obj=Children()
obj.selectBook()