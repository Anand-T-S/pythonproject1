class Student:
    College_name="sdjs"
    def stud_det(self,Student_name,Roll_no,Department):
        self.Student_name=Student_name
        self.Roll_no=Roll_no
        self.Department=Department
    def printvalue(self):
        print("Student_name: ",self.Student_name,"\nRoll_no: ",self.Roll_no)
        print("Department: ",self.Department,"\nCollege_name: ",Student.College_name)
s1=Student()
s1.stud_det("anu",19,"Cs")
s1.printvalue()
print()
s2=Student()
s2.stud_det("amal",20,"Bca")
s2.printvalue()