s=" hello world"
n=input("Enter the str:")
flag=0
for i in s:
    if i==n:
        flag=1
        break
if flag==1:
    print("present")
else:
    print("not present")
