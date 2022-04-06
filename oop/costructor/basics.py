# constructor
# initialize instance variable at the time of object creation

class Student:
    clg="jsfjk"
    def __init__(self,name,rollno,departmnt):
        self.name=name
        self.rollno=rollno
        self.departmnt=departmnt
        # self.clg=clg
    def printval(self):
        print("Name:",self.name,"\nrollno:",self.rollno,"\ndepartmnt:",self.departmnt,"\nCollege:",Student.clg)
s1=Student("anu",23,"bca")
# s1.setvalue()
s1.printval()