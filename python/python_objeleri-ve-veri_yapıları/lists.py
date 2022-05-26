
message = "Hello There. My name is Ikbal Kolay.".split()
    #.split() --> bosluk karekterinden stringi ayırır böylece dizi olusur
# print(message[0])

# myList = [1,2,3]
# print(myList)

list1 = ["one","two","there"]
list2 = ["four","five","six"]

numbers = list1+list2
print(numbers) 
print(len(numbers))
print(message[0])
print(numbers[2])

userA = ["ikbal",22]
userB = ["oguz",20]

users = [userA,userB] # [] içine alındıgında liste icerisinde liste oluyor

print(userA)
print(userB)
print(users)        # --> [['ikbal', 22], ['oguz', 20]]
print(users[0])     # --> ['ikbal',22]
print(users[0][0])  # --> ikbal
