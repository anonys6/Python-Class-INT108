import math

x = int(input())
y = int(input())
z = int(input())

r = ((x ** 2) + (y ** 2) + (z ** 2)) ** (0.5)

print(math.ceil(r))