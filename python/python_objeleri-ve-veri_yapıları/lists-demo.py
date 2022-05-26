cars = ['Bmw','Mercedes','Opel','Mazda']
print(cars)
print(len(cars))
print(f'ilk eleman {cars[0]}, son eleman {cars[-1]}')
cars[-1]='Toyota'
print(cars)
result = 'Mercedes' in cars
print(result)
print(cars[:3])
cars[-2:] = ['Toyota','Renault']
print(cars)
result =cars + ['Audi','Nissan']
print(result)
del cars[-1]
result = cars
print(result)
result = cars[::-1]     # tersten yazdırır
print(result)

studentA = ['yiğit','bilgi',2010,[70,60,70]]
studentB = ['sena','turan',1999,[80,80,70]]
studentC = ['ahmet','turan',1998,[80,70,90]]

result = studentA[0]
result = studentB[1]
result = studentC[3][0]

result = f'{studentA[0]} {studentA[1]} {2022-studentA[2]} yasında ve not ortalması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}'
print(result)
