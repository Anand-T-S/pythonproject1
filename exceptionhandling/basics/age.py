age=int(input("Enter the age: "))
try:
    if age >= 18:
        print("Eligible for vaccination")
except Exception as error:
    print(error)