mylist = [1,2,3]
# myString = "my string"


# print(len(mylist))
# print(len(myString))

class Movie():
    def __init__(this, title, director, duration):
        this.title = title
        this.director = director
        this.duration = duration
        print("movie objesi olusturuldu")

    def __str__(this):
        return f"{this.title} by {this.director}"
    
    def __len__(this):
        return this.duration

    def __del__(this):
        print("movie silindi")

m = Movie("film adı","yönetmen adı", 120)

# print(str(mylist))
# print(str(m))

# print(len(mylist))
# print(len(m))

del m
