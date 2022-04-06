# name,phn,mailid
f=open('userdt.txt','w')
n=input("Enter your name: ")
phn=input("Enter your mobile num: ") #str type is neccesary
m=input("Enter your email id: ")
f.write(n)
f.write("\n")
f.write(phn)
f.write("\n")
f.write(m)