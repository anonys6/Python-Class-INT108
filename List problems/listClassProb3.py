# # a = []

# # length = int(input("How many elements you want inside list: "))

# # for i in range(0, length):
# #     i = input()
# #     if isinstance(i, int):
# #         i = int(i)
# #         a.append(i)
# #         a[i] == int(a[i])
# #     # else:
# #     #     a.append(i)

# # print(type(a[0]))

# # print(a)

# a = input("Enter list element separated by commas: ")
# a = list(a.split(" "))

# # for i in range(0, len(a)):
# #     if type(a[i]) == 'int':
# #         a[i] == int(a[i])

# # print(a)

# # lis = []

# # n = int(input("Enter the list size: "))

# # print("\n")

# # for i in range(0, n):
# #     temp = input()
# #     if type(temp) == type(n):
# #         temp = int(temp)
# #         lis.append(temp)
# #     else:
# #         lis.append(temp)


# # print(lis)

# sum = 0

# lis = a
# for i in lis:
#     if i.isdigit():
#         sum = sum + int(i)


# print(sum)

lis = []

n = int(input("Enter length of the string: "))

sum = 0

for i in range(0, n):
    i = input()
    if i.isdigit():
        i = int(i)
        sum = sum + i
    lis.append(i)


print(lis)
