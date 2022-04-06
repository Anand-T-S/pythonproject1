class Bank:
    Bank_name="SBI"
    acc_no=9885
    acc_bal=0
    def acc_creation(self,name,mob):
        self.name=name
        self.mobile=mob
        Bank.acc_no+=1
    def deposit(self,dep_amt):
        self.dep_amt=dep_amt
        # Bank.acc_bal=acc_bal
        # self.acc_bal=0
        Bank.acc_bal+=dep_amt
    def withdrawal(self,withdraw_amt):
        self.widthdraw_amt=withdraw_amt
        if self.widthdraw_amt<=Bank.acc_bal:
            Bank.acc_bal=Bank.acc_bal-self.widthdraw_amt
        else:
            print("Insufficient Balance")
    def print_acc(self):
        print("Name:",self.name,"\nMobile:",self.mobile,"\nBank Name:",Bank.Bank_name,"Account_no",Bank.acc_no)
        print()
    def print_dept(self):
        print("Acc_bal:",self.acc_bal)
    def print_wdl(self):
        print("current_bal:",Bank.acc_bal)
b1=Bank()
n=input("Enter name:")
p=int(input("Enter mobile no:"))
dt_amt=int(input("deposit_amt:"))
b1.acc_creation(n,p)
b1.print_acc()
b1.deposit(dt_amt)
b1.print_dept()
w_amt=int(input("Withdrawal_amt:"))
b1.withdrawal(w_amt)
b1.print_wdl()