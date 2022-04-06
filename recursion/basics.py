# recursion

# n=int(input("Enter the num"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
n=int(input("Enter the number: "))
print(fact(n))