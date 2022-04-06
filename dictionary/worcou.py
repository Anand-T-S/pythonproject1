# hello hi hello hi world
# count={"hello":2,"hi":2,"world":1}

s=input("Enter string")
count={}
data=s.split(" ")
for word in data:
    if word not in count:
        count.update({word:1})  #hello:1 hai:1
    else:
        val=count[word]
        val+=1
        count.update({word:val})
print(count)
