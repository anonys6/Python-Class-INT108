import string

# METHOD 1

a = input("Enter list element separated by commas: ")
a = list(a.split(" "))

a = [eval(i) for i in a]

print("List is:", a)

a.sort()

print("After sorting:", a)

print("Highest element", a[-1])
print("Lowest element", a[0])


# METHOD 2

# stra = input("Enter list element separated by commas: ")
# stra = list(stra.split(" "))

# for i in range(0, len(stra)):
#     stra[i] == int(stra[i])

# print("List is:", stra)

# stra.sort()

# print("after sorting:", stra)

# print("Highest element", stra[-1])
# print("Lowest element", stra[0])