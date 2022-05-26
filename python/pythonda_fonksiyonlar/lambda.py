# def square (num):
#     return num**2

# print(square(2))
# # 4

#     # map 
# """ map methodu ya bir liste ile çevrilmeli ya da for bloğu içinde kullanılmalı """

# numbers = [1,3,5,9]
# result = list(map(square,numbers))
# print(result)
# # [1, 9, 25, 81]

# for item in map(square,numbers):
#     print(item)
"""
1
9
25
81
"""


    # lambda
""" sadece 1 kez kullanılacak bir fonksiyon tanımlamak yerine (isimsiz bir ifade)lambdayı kullanırız"""

# numbers = [1,3,5,9]
# result = list(map(lambda num: num**3,numbers))
# print(result)
# #[1, 27, 125, 729]

    # filter
def check_even(num): return num % 2 == 0
numbers = [1,2,3,4,5]
result = list(filter(check_even,numbers))
print(result)
# [2, 4]

# def check_even(num): return num % 2 == 0
numbers = [1,2,3,4,5]
result = list(filter(lambda num: num%2==0,numbers))
print(result)
# [2, 4]