import re
rule="[A-Z][\w]{3,8}[A-Z]"
s=input("Enter a String:")
matches=re.fullmatch(rule,s)
if matches is not None:
    print("valid")
else:
    print("Invalid")