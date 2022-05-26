# class

from turtle import circle


class Person:
    #class atributes
    address = "no information"
    #constructor (yapıcı method) oluşturulan her obje için çalıştırılır,mutlaka eklenmesini istediklerimizi burada yapıyoruz
    def __init__(self, name ,year): # self --> class'tan türetilen herhangi bir objeyi tesil eder
        #object attributes  
        self.name = name
        self.birthyear = year
        print("init methodu çalıştı..")
    #instance methods
    def intro(self):
        print("hello there. I am "+ self.name)
    
    def calculaterAge(self):
        return 2022-self.birthyear


# object , instance
p1 = Person("ikbal",1999)
p2 = Person("samet",2000)

p1.intro()
p2.intro()

print(f"{p1.name} age: {p1.calculaterAge()}")
print(f"{p2.name} age: {p2.calculaterAge()}")



class Circle:
    #class object attributes
    pi = 3.14
    
    def __init__(self,yaricap=1):
        self.yaricap = yaricap
    
    # methods

    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)

c1 = Circle() #yaricap belirtmezsek = 1 olur
c2 = Circle(5)

print(f"c1: alan = {c1.alan_hesapla()} cevre = {c1.cevre_hesapla()}")
print(f"c2: alan = {c2.alan_hesapla()} cevre = {c2.cevre_hesapla()}")