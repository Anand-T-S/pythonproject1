s=input("Enter the string: ")
n=""
r="a,b,c,d,e"
for i in s:
    if i not in r:
        n+=i
print(n)