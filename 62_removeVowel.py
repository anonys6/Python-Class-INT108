a = input()

v = ["a", "e", "i", "o", "u"]

for i in range(0, len(a)):
    if a[i] in v:
        continue
    print(a[i], end=" ")