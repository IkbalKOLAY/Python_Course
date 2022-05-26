import random 

sayı = random.randint(1,10)

hak = int(input("kac hak kullanmak istersiniz:"))
sayac = 0
while(hak>0):
    hak -= 1
    sayac += 1
    tahmin = int(input("tahmin: "))

    if sayı == tahmin:
        print(f"{sayac}. defada bildiniz tebrikler!. Toplam puanınız: {100-(100/hak)*(sayac-1)}")
        break
    elif sayı>tahmin:
        print("yukarı")
    else:
        print("asagı")
    if hak == 0:
        print(f"hakınız bitti. sayı:{sayı}")