from numpy import number

numbers = []
for x in range(0,10):
    numbers.append(x)
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers_=[x for x in range(10)]
print(numbers_)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in range(10):
    print(x**2)
numbers_ = [x**2 for x in range(10)]
print(numbers_)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

numbers = [x*x for x in range(10) if x % 3 ==0]
print(numbers)
# [0, 9, 36, 81]

myString = "hello"
mylList = []
for letter in myString:
    mylList.append(letter)
print(mylList)
#['h', 'e', 'l', 'l', 'o']

mylList = [letter for letter in myString]
print(mylList)
# ['h', 'e', 'l', 'l', 'o']


years = [1999,2000,2002,2021]
ages = [2022 - year for year in years]
print(ages)
#[23, 22, 20, 1]

result = [x if x%2==0 else 'TEK' for x in range(1,10)]
print(result)
#['TEK', 2, 'TEK', 4, 'TEK', 6, 'TEK', 8, 'TEK']

result = [x for x in range(1,10)if x%2==0]
print(result)
#[2, 4, 6, 8]

result=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)
#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)] 

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)
#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)] 
