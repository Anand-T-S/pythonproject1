# a={1,2,3,4}
# b={1,3,6,7,8}
# for i in a:
#     if i in b:
#         print(i)

a={1,2,3,4}
b={1,3,6,7,8}
com=set()
for i in a:
    if i in b:
        com.add(i)
print(com)