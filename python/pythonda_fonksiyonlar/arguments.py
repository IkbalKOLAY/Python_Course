
# def changeName(n):
#     n= "ADA"

# name = "yigit"
# changeName(name)
# print(name)
# # yigit



# def change(n):
#     n[0] = "istanbul"

# sehirler = ["ankara","adana"]
# change(sehirler)
# print(sehirler)
# # ['istanbul', 'adana']



# def add(a,b,c=0):  # 4 veya daha fazla parametreyi toplamak istediğimizde sıkıntı olucak
#     return sum((a,b,c)) 

# print(add(10,20))
# print(add(10,20,12))


# def add(*prm):  # istediğimiz kadar parametre gönderebiliriz (tuple)
#     return sum((prm)) 

# print(add(10,20))
# print(add(10,20,45,49))


# def displayUser(**params): # ** -> dictionary
    
#     for key,value in params.items():
#         print("{} is {}".format(key,value))

# displayUser(name="ikbal", age=22, city="trabzon")
# displayUser(name="samet", age=21, city="ankara")
# displayUser(name="hatice", age=21, city="aydin")


def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,key1 ="value 1", key2 = "value 2")