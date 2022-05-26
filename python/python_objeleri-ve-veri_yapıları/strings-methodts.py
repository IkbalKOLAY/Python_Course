from email import message


message = " Hello there. My name is ikbal kolay"
print(message)
message= message.upper()        # bütün karakterleri büyütür
print(message)
message= message.lower()        # bütün karakterleri küçültür
print(message)  
message=message.title()         # bütün kelimenin bası büyük olur
print(message)
message=message.capitalize()    # ifadenin ilk harfi büyük olur
print(message)
message=message.strip()         #ifadenin basındaki bosluk silinir
print(message)
message=message.split()         #string ifade her bosluktan bölünür dizi olusur 
print(message)
message=" ".join(message)       #ayrılmıs olan ifadeyi aralara bosluk ekleyerek birlestir
print(message)

index=message.find("ikbal")         #aradıgım kelimeyi bulmaya calısır (-1 ise yoktur)
print(index)
isFound= message.startswith("H")    #H ile mi baslıyor?
print(isFound)
isFound2=message.endswith("y")      #n ile mi bitiyor?
print(isFound2)

message= message.replace("ikbal","oguz")     #ikbal yerine oguz yaz
print(message)
# message=message.replace(" ","*")    #bolsuk karakterleri yerine * koyar
# print(message)
# message=message.center(100)     #mesajı 100 karakterlik alana yerlestir
# print(message)
message=message.center(50,"*")     #mesajı 50 karakterlik alana yerlestir bosluklara * koy
print(message)
