f=open('data.txt','r')
l=[]
for i in f:
    words=i.rstrip("\n").split(" ")
    l.extend(words)
print(l)
count={}
for i in l:
    if i not in count:
        count.update({i:1})
    else:
        val=count[i]
        val+=1
        count.update({i:val})
print(count)