#self keyword used to point to the current instance
class Display_numbers:
    def getnumber(self,no1,no2): #insatance method
        self.no1=no1             #instance variables
        self.num2=no2
    def print_number(self):
        print(self.no1)
        print(self.num2)
d1=Display_numbers()
d1.getnumber(5,8)
d1.print_number()