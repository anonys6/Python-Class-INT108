import string

a = input("Enter list a element separated by commas: ")
b = input("Enter list b element separated by commas: ")
a = list(a.split(" "))
b = list(b.split(" "))

count = 0

for i in a:
    for j in b:
        if i == j:
            count = count + 1
            a.remove(i)
            b.remove(j)
if count > 0:
    print("List after removing all the common elements:")
    print("a:", a)
    print("b:", b)
else:
    print("No common element:")
    print("a:", a)
    print("b:", b)