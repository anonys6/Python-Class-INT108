import math

def lcmfun(a, b):
    return math.lcm(a, b) ** 3


a = int(input())
b = int(input())

print(lcmfun(a, b))
