
ogrenciler = {}


number = input('öğrenci no: ')
name = input('öğrenci adı: ')
surname = input('öğrenci soyadı: ')
phone = input('öğrenci telefon: ')

ogrenciler.update({     # update metodu sayesinde bircok veri ekleyebiliriz
    number:{
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

ogrenciler[number] = {
    'ad': name,
    'soyad': surname,
    'telefon': phone
}



print(ogrenciler)