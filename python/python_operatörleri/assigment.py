# x = 5
# y = 10
# z = 20

x, y, z= 5, 10, 20

# x,y=y,x

x += 5      # x = x + 5
x -= 5      # x = x - 5
x *= 5      # x = x * 5
x /= 5      # x = x / 5

# print(x,y,z)

# values = (1,2,3)
# print("values:",values)
# print(type(values))
# x,y,z = values
# print(x,y,z)

values_ = 1,2,3,4,5
print("values_:",values_)
print(type(values_))
x,y,*z = values_
print(x,y,z)
print(x,y,z[2])