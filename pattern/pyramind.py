x=6
for i in range(5,0,-1):
    for k in range(x):
        print(end=" ")
    x+=1
    for j in range(i):
        print("*",end=" ")
    print()