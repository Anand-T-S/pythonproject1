import re
f=open("phone.txt","r")
rule = '[+][9][1][\d]{10}'
for i in f:
    n=i.rstrip("\n")
    match = re.fullmatch(rule,n)
    if match is not None:
        print(n)
