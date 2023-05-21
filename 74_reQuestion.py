
a = input()
b = input()

lis1 = list(map(int, a.split(",")))
lis2 = list(map(int, b.split(",")))

lisSum = []

for i in range(len(lis1)):
    temp = lis1[i] + lis2[i]
    lisSum.append(temp)

print(lisSum)