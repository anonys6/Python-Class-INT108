lis = [2, 4, 6]

lis.append(8)
lis.append(10)

print("after append:", lis)

lis.sort()

print("list after sorting:", lis)

sum = 0
for i in lis:
    sum = sum + i

print("sum of list is:", sum)

print("max of list:", max(lis), ", and lowest is:", min(lis))

print(lis.count(2))

lis.reverse()
print(lis)

lis.reverse()

for i in lis:
    print(len(str(i)), end=", ")

