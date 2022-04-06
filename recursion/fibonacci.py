# 0,1,1,2,3
def rfibo(n):
    if n<=1:
        return n
    else:
        return rfibo(n-1)+rfibo(n-2)
for i in range(10):
    print(rfibo(i))