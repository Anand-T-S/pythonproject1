class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printPerson(self):
        print(self.name,self.age,self.place)
class Child:
    def __init__(self,std,school):
        self.std=std
        self.school=school
    def printchild(self):
        print(self.std,self.school)
class Student(Person,Child):
    def __init__(self,rollno,dprt,name,age,place,std,school):
        Person.__init__(self, name, age, place)
        Child.__init__(self, std, school)
        self.rollno=rollno
        self.dprt=dprt
    def printstudent(self):
        print(self.rollno,self.dprt)
st=Student(1,"csc","anu",22,"kochi",12,"dps school")
st.printPerson()
st.printchild()
st.printstudent()
