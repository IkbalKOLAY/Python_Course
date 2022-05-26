# x = "global x"
# def function():
#     x = "local x"
# function()
# print(x)


#global
# name = "ikbal"
# def change_name(new_name):
#     #local
#     name = new_name
#     print(name)

# change_name("samet")
# print(name)


# name = "global string"
# def greeting():
#     #name = "ikbal"
#     def hello():
#         #name = "samet"
#         print("hello "+name)
#     hello()
# greeting()

from re import X


x = 50
def test():
    global x
    print(f"x : {x}")

    x = 100
    print(f"changed x to: {x}")

test()
print(x)

# global olarak tanımlamasaydık x değeri hala 50 olarak kalırdı yani def bloğu içindeki
# hic bir değişiklikten yararlanmazdı