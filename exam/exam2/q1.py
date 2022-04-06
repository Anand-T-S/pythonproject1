class Vehicle:
    def __init__(self,category,fuel):
        self.category=category
        self.fuel=fuel
    def printvehicle(self):
        print(self.category,self.fuel)
class Bus(Vehicle):
    def __init__(self,category,fuel,regno,chaseno):
        super().__init__(category,fuel)
        self.regno=regno
        self.chaseno=chaseno
    def printbus(self):
        print(self.category,self.fuel,self.regno,self.chaseno)
b1=Bus("HPMV/HTV","Diesel","KL08BN2345","600687B")
b1.printbus()