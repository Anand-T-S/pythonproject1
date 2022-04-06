def sum(l):
    s=0
    for i in range(1,l+1):
        s+=i
    return s
num=int(input("Enter the number:"))
print(sum(num))