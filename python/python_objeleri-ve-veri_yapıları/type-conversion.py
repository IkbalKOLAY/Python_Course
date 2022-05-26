
# input'tan gelen değer stirng olarak atanır

"""
x = input('1.sayı: ')
y = input('2.sayI: ')
toplam = int(x) + int(y) 
print(toplam)

"""

from lib2to3.pgen2.token import NEWLINE


x = 5               # int
y= 2.5              #float
name = "ikbal"      #string
isOnline = True     #bool

        # type-conversion

# int to float 

x = float(x)
print(x)
print(type(x))

# float to int

y = int(y)
print(y)
print(type(y))

# bool to string

# isOnline = str(isOnline)
# print(isOnline)
# print(type(isOnline))

# bool to int

isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))

print("************************")
pi = 3.14
r = float(input("yarı cap: "))
alan = pi*(r**2)
cevre = 2*pi*r
print("alan :" ,alan)
print("cevre:" ,cevre)


