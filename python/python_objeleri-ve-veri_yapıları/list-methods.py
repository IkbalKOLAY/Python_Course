numbers = [1,10,5,16,4,9,10]
letters =['a','g','s','b','y','a','s']

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4]=40
numbers.append(49)              # listenin sonuna eleman ekler
numbers.append(59)
numbers.append(52)
numbers.insert(3,78)            # istenilen indexe eleman ekler
# numbers.insert(-1,52)
# numbers.pop(0)                # istenilen indexteki elemanı siler
# numbers.pop(-1)
# numbers.remove(49)            # istenilen elemanı siler

numbers.sort()                  # sıralar
numbers.reverse()               # tersine döndürür

letters.sort()
letters.reverse()

print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(10))        # istediğimiz elemanın sayısını öğrenebiliriz
print(letters.count('a'))

numbers.clear()                 # bütün elemanları silmek için kullanılır
print(numbers)