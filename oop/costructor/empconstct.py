class Employee:
    Company_name="K&K"
    def __init__(self,emp_name,emp_id,Desig,Salary):
        self.Employee_name=emp_name
        self.Emp_id=emp_id
        self.Designation=Desig
        self.Salary=Salary
    def print_value(self):
        print("Emp Name: ",self.Employee_name,"\nEmp_id: ",self.Emp_id,"\nDesignation: ",self.Designation)
        print("Salary: ",self.Salary,"\nCompany Name: ",Employee.Company_name)
        print()
emp1=Employee("anu",988,"Db",25000)
# emp1.emp_det()
emp1.print_value()

emp2=Employee("alan",997,"Designer",28000)
# emp2.emp_det()
emp2.print_value()