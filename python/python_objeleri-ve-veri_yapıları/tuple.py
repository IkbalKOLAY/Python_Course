list = [1, 2, 3]
tuple = (1, 'iki', 3)

print(type(list))
print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(tuple))
# print(len(list))

list = ['ali','veli']
tuple = ('damla','ayse','ayse')
names = ('demet','emel','ayse') + tuple

list[0] = 'ahmet'
# tuple[0] = 'deniz'  # tuple listelere sonradan atama yapamayız

print(list)
print(tuple)
print(names)

result = tuple.count('ayse')
print(f'ayse kac kere tekrarlanır : {result} ')
_result = tuple.index('ayse')
print(f'ayse kacıncı indexte : {_result}')





