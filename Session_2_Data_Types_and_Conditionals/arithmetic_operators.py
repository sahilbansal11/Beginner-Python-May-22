
# Arithmetic operators

a = int(input()) # 8, 8
b = int(input()) # 4, 5

c = a - b
print(c) # 4, 3

d = a * b
print(d) # 32, 40

e = a / b # division will always give you a float
print(e) # 2.0, 1.6

print(type(e))

# 8 / 5 = 1.6
# you want to just print the integer value of it, i.e. 1

print(int(e)) # we are converting a float to an int

print(1.6) # float

print('123') # str

print(int('123')) # int

print(int(1.6)) # it just removes the decimal part

print(int(-1.6)) # it just removes whatever is after the dot