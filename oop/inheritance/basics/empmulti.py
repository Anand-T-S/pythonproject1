class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printPerson(self):
        print(self.name,self.age,self.place)
class Parent(Person):
    def setparent(self,add,phn):
        self.address=add
        self.phone=phn
    def printParent(self):
        print(self.address,self.phone)
class Employee(Parent,Person):
    def setEmployee(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
    def printEmployee(self):
        print(self.id,self.desig,self.salary)
emp=Employee()
emp.setEmployee(9987,"AE",90000)
emp.setparent("street1",685465456)
emp.setperson("anu",21,"kochi")
emp.printPerson()
emp.printParent()
emp.printEmployee()