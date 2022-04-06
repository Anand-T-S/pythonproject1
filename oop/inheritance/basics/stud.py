class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printPerson(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def setstudent(self,rollno,dprtmnt):
        self.rollno=rollno
        self.department=dprtmnt
    def printStudent(self):
        print(self.name,"rollno",self.rollno,self.department)
st=Student()
st.setperson("anu",23,"kochi")
st.setstudent(2,"cse")
st.printStudent()
st.printPerson()