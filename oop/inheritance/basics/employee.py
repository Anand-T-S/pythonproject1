class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printPerson(self):
        print(self.name,self.age,self.place)
class Employee(Person):
    def setEmployee(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
    def printEmployee(self):
        print(self.id,self.desig,self.salary)
emp=Employee()
emp.setperson("anu",23,"kochi")
emp.setEmployee(2,"asd",250)
emp.printPerson()
emp.printEmployee()