from cgitb import reset
import random


# result= dir(random)
# result = help(random)

result = random.random() # 0.0 - 1.0
result = random.random() *100
result = int(random.uniform(10,100)) # int() içine alarak ondalık kısımdan koruduk
 
result = random.randint(1,200) # ondalık kısım olmadan sayı üretiyor

greeting = "hello there"
names = ["ikbal","samet","hamza","erto","selami","hatice"]

result = names[random.randint(0,len(names)-1)]
# choice random modülü üzerinden kullanılan daha efective bir secenek
result = random.choice(names)
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)
# [1, 7, 5, 4, 8, 6, 9, 2, 0, 3]

liste = range(100)
result = random.sample(liste,3)
[26, 29, 49]

print(result)
# print(liste)