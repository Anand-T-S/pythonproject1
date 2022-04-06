class Teacher:
    def __init__(self,T_name,id,deptmnt,sub):
        self.T_name=T_name
        self.Id=id
        self.department=deptmnt
        self.subject=sub
    def print_val(self):
        print("Teacher_Name: ",self.T_name,"\nTeacher_Id: ",self.Id)
        print("Department: ",self.department,"\nSubject: ",self.subject)
t1=Teacher("rena","6532","science","Maths")
t1.print_val()