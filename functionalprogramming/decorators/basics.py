# def eligibility(func):
#     def wrapper(a,b):
#         if b>=18:
#             return func(a,b)
#         else:
#             raise Exception("not eligible")
#     return wrapper
# @eligibility
# def vaccinecheck(name,age):
#     return "you can vaccinate"
# print(vaccinecheck("amal",23))


def usercheck(func):
    def wrapper(a,b):
        if a=="admin":
            return func(a,b)
        else:
            raise Exception("not allowed")
    return wrapper
@usercheck
def change_pin(username,pin):
    mypin=pin
    return pin
# print(change_pin("user1",8766))
print(change_pin("admin",8566))