# İnheritance ( kalıtım) : miras alma

class Person:
    def __init__(this,fname,lname):
        this.firstname = fname
        this.lastname = lname
        print("person created")

    def whho_am_i(this):
        print("ı am a person")

    def eat(this):
        print("ı am eating")
    
class Student(Person):
    def __init__(this,fname,lname,number):
        Person.__init__(this,fname,lname)
        this.studentNumber = number
        print("student created")

    # overriding
    def whho_am_i(this):
        print("ı am a student")
    
    def sayHello(this):
        print("hello ı am a student")

class Teacher(Person):
    def __init__(this, fname, lname,branch):
        super().__init__(fname, lname)
        this.bracnh = branch
    
    def who_am_i(this):
        print(f"ı am a {this.bracnh} teacher")


        
p1 = Person("ikbal","kolay")  # person created
s1 = Student("ikbal","kolay",383250) # person created student created
t1 = Teacher("hatice","kovan","math")

print(p1.firstname+" "+p1.lastname)
print(s1.firstname+" "+s1.lastname+" "+str(s1.studentNumber))
print(t1.firstname+" "+t1.lastname+" "+ t1.bracnh)

p1.whho_am_i()
s1.whho_am_i()

s1.eat()
s1.sayHello()

t1.whho_am_i()