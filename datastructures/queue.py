queue=[]
size=int(input("Enter size: "))
front=0
rear=0
def enqueue():
    global size,front,rear
    if rear>=size:
        print("Queue is full")
    else:
        e=int(input("Enter element"))
        queue.insert(rear,e)
        rear+=1
        for i in range(front,rear):
            print(queue[i])
def dequeue():
    global size,front,rear
    if front==rear:
        print("queue is empty")
    else:
        front+=1
        for i in range (front,rear):
            print(queue[i])
while True:
    opt=int(input("select operation..\n1.enqueue\n2.dequeue"))
    if opt==1:
        enqueue()
    elif opt==2:
        dequeue()
    else:
        print("invalid option")
        break
