# 10.what is list comprehension?
# use list comprehension to create a list with elements 1-100 that are divisible by 5?
# l=[]
# for i in range(1,100):
#     if i%5==0:
#         i=l.append(i)
# print(l)

l=[i for i in range(1,100) if i%5==0]
print(l)

