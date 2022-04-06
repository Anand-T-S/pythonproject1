class Bookdetails:
    def details(self,name,author,pages):
        self.name=name
        self.author=author
        self.pages=pages
    def print_det(self):
        print("Name  : ",self.name,"\nAuthor: ",self.author,"\nPages : ",self.pages)
b1=Bookdetails()
b1.details("abc","pqr",234)
b1.print_det()