# def write(word,n):
#     print(word*n)
# write("merhaba\n",10)

def listeyeCevir(*args): # * --> sınırsız sayıda
    liste=[]
    for arg in args:
        liste.append(arg)
    return liste

result=listeyeCevir(10,20,30,"merhaba")
print(result)

