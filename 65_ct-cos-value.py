import math

a = int(input())
b = int(input())

for i in range(a, b + 1):
    print(format(math.cos(i), '.2f'))