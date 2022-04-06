stk=[]
size=int(input("Enter size: "))
top=0
def push():
    global top,size
    if top>=size:
        print("stack is full")
    else:
        ele=int(input("Enter ele: "))
        stk.append(ele)
        top+=1
        print(stk)
def pop():
    global top,size
    if top<=0:
        print("stack is empty")
    else:
        stk.pop()
        print(stk)
        top-=1
while True:
    e=int(input("select operation..\n1.push()\n2.pop()"))
    if e==1:
        push()
    elif e==2:
        pop()
    else:
        print("invalid operation.select correct one..")
        break