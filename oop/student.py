# name,roll no, department,college name
class Student:
    def stud_det(self,Student_name,Roll_no,Department,College_name):
        self.Student_name=Student_name
        self.Roll_no=Roll_no
        self.Department=Department
        self.College_name=College_name
    def printvalue(self):
        print("Student_name: ",self.Student_name,"\nRoll_no: ",self.Roll_no)
        print("Department: ",self.Department,"\nCollege_name: ",self.College_name)
        print()
s1=Student()
s1.stud_det("anu",19,"Cs","sdjs")
s1.printvalue()

s2=Student()
s2.stud_det("amal",20,"Bca","sdjs")
s2.printvalue()

