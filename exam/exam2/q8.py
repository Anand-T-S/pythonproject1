#finally block will be executed no matter if try block raises an exception or not
n1=int(input("n1"))
n2=int(input("n2"))
try:
    print(n1/n2)
except:
    print("exception occured")
finally:
    print("code end")