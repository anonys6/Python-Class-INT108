# import math
# n = int(input())

# stLis = []

# for i in range(1, n + 1):
#     num = i
#     sum = 0
#     while num > 0:
#         sum = sum + math.factorial(num % 10)
#         num = num // 10
#     if sum == i:
#         stLis.append(i ** 2)

# print(stLis)



import math

n = int(input())

stLis = []

for i in range(1, n + 1):
    num = 