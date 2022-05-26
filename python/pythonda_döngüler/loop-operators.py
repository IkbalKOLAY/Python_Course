
#******range********

# # for item in range(10): # 0 dan 10 a kadar yazar [0,9]
# #     print(item)

# for item in range(5,100,10):
#     print(item)

# print(list(range(5,100,10))) # verilen aralıktakileri liste yapar -> [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]



#  ****** enumerate********

greeting = "hello there"

index = 0
# for letter in greeting:
#     print(f'index:{index} > letter:{letter}')
#     index += 1
"""
index:0 > letter:h
index:1 > letter:e
index:2 > letter:l
index:3 > letter:l
index:4 > letter:o
index:5 > letter:
index:6 > letter:t
index:7 > letter:h
index:8 > letter:e
index:9 > letter:r
index:10 > letter:e

"""

# for index, item in enumerate(greeting):
#     #print(item)
#       """
#         (0, 'h')
#         (1, 'e')
#         (2, 'l')
#         (3, 'l')
#         (4, 'o')
#         (5, ' ')
#         (6, 't')
#         (7, 'h')
#         (8, 'e')
#         (9, 'r')
#         (10, 'e')
#       """


# for index, item in enumerate(greeting):
#     print(f'index:{index}  letter:{item}')
    # """
    # index:0  letter:h
    # index:1  letter:e
    # index:2  letter:l
    # index:3  letter:l
    # index:4  letter:o
    # index:5  letter:
    # index:6  letter:t
    # index:7  letter:h
    # index:8  letter:e
    # index:9  letter:r
    # index:10  letter:e
    # """


#**********zip*************
# farklı listeler birleştiriliyor

list1=[1,2,3,4,5]
list2=['a','b','c','d','e']

# print(list(zip(list1,list2)))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

for item in zip(list1,list2):
    print(item)
    """
    (1, 'a')
    (2, 'b')
    (3, 'c')
    (4, 'd')
    (5, 'e')
    """