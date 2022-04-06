l=[1,2,3,4,5,6]
prime=[]
nonprime=[]
for n in l:
    for i in range(2,n):
        if n%i==0:
            nonprime.append(n)
            break
    else:
        prime.append(n)
print(prime)
print(nonprime)
