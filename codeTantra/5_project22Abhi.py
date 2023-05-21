

n = int(input("enter no. of students: "))
a = []
multi = []
arev = []
list1 = []
for i in range(n):
    b = []
    b1 = []
    c = input("name of student: ")
    d = int(input("marks of student: "))
    b.append(c)
    b.append(d)
    b1.append(d)
    b1.append(c)
    a.append(b)
    multi.append(b1)
    arev.append(b1)
print(a)
# nc = no. of changes
nc = int(input("no. of changes"))
for j in range(nc):
    # uname = name to be updated
    # su = score to be updated by
    uname = input("name to be updated")
    su = int(input("score to be updated by"))
    for k in range(len(a)):
        if uname == a[k][0]:
            a[k][1] = a[k][1]+su
            list1.append(a[k][0])
        if uname == arev[k][1]:
            arev[k][0] = arev[k][0]+su
x = sorted(arev)
m = sorted(multi)
print(a)
print(arev)
print(x)
print(list1)
for l in range(len(list1)):
    for y in range(len(a)):
        if list1[l] == m[y][1]:
            print("previous position of", list1[l], "is", n-y)
        if list1[l] == a[y][0]:
            print("position after updation of", list1[l], "is", n-y)
        else:
            continue