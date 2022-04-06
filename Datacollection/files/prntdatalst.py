f=open('data.txt','r')
for i in f:
    words=i.rstrip("\n").split(" ")
    print(words)