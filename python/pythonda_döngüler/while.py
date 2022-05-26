

# x = 1 
# while x <= 100:
#     if x%2==0:
#         print(x)
#     x += 1
# print("bitti...")



name = "" # false

while not name.strip():   #true olur #.strip() metodu boşluk eklenmesini önler
    name = input("isim:")

print(f"merhaba {name}")