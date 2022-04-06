# r=6
# for i in range(r):
#     print(' '*(r-i)+' *'*(i+1))
# for j in range(r-1):
#     print(' '*(j+2)+" *"*(r-1-j))

p=6
# q=1
for i in range(6):
    for k in range(p):
        print(end=" ")
    p-=1
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(6,0,-1):
    for k in range(p):
        print(end=" ")
    p+=1
    for j in range(i):
        print("*",end=" ")
    print()