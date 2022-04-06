import re
rule="^a[\d]{5}b$"
s=input("Enter a String: ")
matches=re.fullmatch(rule,s)
if matches is not None:
    print("valid")
else:
    print("Invalid")