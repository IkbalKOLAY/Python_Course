class Person:
    #class atributes
    address = "no information"
    #constructor (yapıcı method) oluşturulan her obje için çalıştırılır,mutlaka eklenmesini istediklerimizi burada yapıyoruz
    def __init__(self, name ,year): # self --> class'tan türetilen herhangi bir objeyi tesil eder
        #object attributes  
        self.name = name
        self.birthyear = year
        print("init methodu çalıştı..")
    #methods
    def intro():
        print("hello there")


# object , instance
p1 = Person("ikbal",1999)
p2 = Person("samet",2000)
# accesing object attributes
print(f"p1: name :{p1.name} year: {p1.birthyear} address: {p1.address}")
print(f"p2: name :{p2.name} year: {p2.birthyear} address: {p2.address}")
