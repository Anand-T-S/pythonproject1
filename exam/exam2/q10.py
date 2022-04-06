import re
rule='^[A-Z][a-z\W]*'
s=input("Enter a String:")
match=re.fullmatch(rule,s)
if match is not None:
    print("valid")
else:
    print("Invalid")