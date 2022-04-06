b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
count=0
for i in b:
    count+=1
mid=(count-1)/2
print("mid element is:",b[int(mid)])
r=b[int(mid)]
b.remove(r)
print(b)