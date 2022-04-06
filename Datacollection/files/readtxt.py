f=open('example.txt','r')
# print(f)
for i in f:
    # print(i)
    a=i.rstrip("\n")
    print(a)