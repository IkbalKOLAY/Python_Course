"""
    1. indekslenemezler
        print(fruits[0])
    2. tüm elemanlara ulaşmak istenildiğinde döngüler kullanılmalı
        for x in fruits:
        print(x)
    3. elemanlar tekrarlanmaz
"""

fruits = {'orange','apple','banana'}

print(fruits)

for x in fruits:
    print(x)


fruits.add('cherry')                 # tek eleman ekleme
print(fruits)     

fruits.update(['mango','grape'])    # update metodu sayesinde liste göndererek ekleme
print(fruits)

fruits.add('apple')                 # daha önce eklenmis eleman tekrar ekranda gösterilmez
print(fruits)   

fruits.remove('mango')              # eleman silme
fruits.discard('apple')             # eleman silme
print(fruits)

fruits.pop()
fruits.clear()      # tüm elemanları siler
print(fruits)   
