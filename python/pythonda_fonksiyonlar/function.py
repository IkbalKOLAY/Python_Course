
# def sayHello(name= "user"):
#     print("hello " + name)

# sayHello("ikbal")   # parametre olursa  -> hello ikbal
# sayHello()          # parametre olmazsa -> hello ikbal


# return  --->>> fonskiyonu çağırırken bir değişkene atamalıyız
# def sayHello(name= "user"):
#     return ("hello " + name)

# msg = sayHello("ikbal")
# print(msg)


# def total(num1,num2):
#     return num1+num2

# result = total(10,20)
# print(result)


def yasHesapla(dgmYili):
    return 2022-dgmYili

# ageİkbal = yasHesapla(1999)
# print(ageİkbal)

def EmekliligeKacYilKaldi(dgmYili, isim):
    yas = yasHesapla(dgmYili)
    emeklilik = 65-yas
    if(emeklilik>0):
        print(f"sayın {isim}, emekliliğinize {emeklilik} yıl kaldı")
    else:
        print(f"sayın {isim}, zaten emekli oldunuz")

EmekliligeKacYilKaldi(1950,"samet")




