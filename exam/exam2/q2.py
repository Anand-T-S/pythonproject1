class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printPerson(self):
        print(self.name,self.age,self.place)
class Child(Person):  #single
    def setchild(self,name,dob):
        self.chname=name
        self.dob=dob
    def printchild(self):
        print(self.chname,self.dob)
class Parent:
    def setparent(self,add,phn):
        self.address=add
        self.phone=phn
    def printParent(self):
        print(self.address,self.phone)
class Student(Child):
    def Student(self,stname,div,schname):
        self.stname=stname
        self.div=div
        self.schname=schname
class Employee(Person,Parent):
    def setEmployee(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
    def printEmployee(self):
        print(self.id,self.desig,self.salary)
ch=Child()
ch.setperson("anu",21,"kochi")
ch.setchild("jo","12feb2020")
ch.printPerson()
ch.printchild()
emp=Employee()
emp.setperson("abc",40,"tcr")
emp.setEmployee(122,"MD",500000)
emp.printPerson()
emp.printEmployee()
