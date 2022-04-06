a=[1,2,3]
i=int(input("Enter index: "))
try:
    print(a[i])
# except:
#     print("exception......\nlist index out of range")
except Exception as error:
    print(error)