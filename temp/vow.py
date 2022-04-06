s=input("enter a string: ")
vow="aeiou"
rst=""
for i in s:
    if i not in vow:
        rst+=i
print(rst)