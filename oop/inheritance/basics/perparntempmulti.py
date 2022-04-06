class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printPerson(self):
        print(self.name,self.age,self.place)
class Parent(Person):
    def __init__(self,add,phn,name,age,place):
        super().__init__(name,age,place)
        self.address=add
        self.phone=phn
    def printParent(self):
        print(self.address,self.phone)
class Employee(Parent):
    def __init__(self,id,desig,salary,name,age,place,add,phn):
        Parent.__init__(self,name,age,place, add, phn)
        # Person.__init__(self, name, age, place)
        self.id=id
        self.desig=desig
        self.salary=salary
    def printEmployee(self):
        print(self.id,self.desig,self.salary)
emp=Employee(45,"dev",25000,"amal",23,"kch","ssds",63666636)
emp.printPerson()
emp.printParent()
emp.printEmployee()
