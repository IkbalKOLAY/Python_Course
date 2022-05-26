
# elemanlar üzerinde güncelleme yapabiliyoruz

"""
plakalar = {'kocaeli': 41, 'istanbul': 34}
print(plakalar['kocaeli'])
print(plakalar['istanbul'])

plakalar['ankara'] = 6
plakalar['kocaeli'] = 'new value'
print(plakalar)

"""

users ={                                    # users={ 'key' : value }
    'ikbalkolay'    :{                      # value kısmıda alt bilgilere ayrılıyor
        'age'       : 22,
        'email'     : 'ikbalkolay@gmail.com',
        'address'   : 'adana'
    },
    'haticekovan'   :{
        'age'       : 21,
        'email'     : 'haticekovan@gmail.com',
        'address'   : 'aydın'
    },
    'fatmanurkaya'  :{
        'age'       : 23,
        'email'     : 'fatmanurkaya@gmail.com',
        'address'   : 'gaziantep'
    }
}

print(users)
print(users['ikbalkolay'])
print(users['ikbalkolay']['email'])