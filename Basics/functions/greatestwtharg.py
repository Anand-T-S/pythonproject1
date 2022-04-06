#greatest of 2 num
def greatest(v1,v2):
    if v1>v2:
        return("n1 greatest")
    else:
        return ("n2 greatest")
n1=int(input("Enter n1"))
n2=int(input("Enter n2"))
print(greatest(n1,n2))
