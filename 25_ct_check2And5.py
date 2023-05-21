
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

def check(x):
    if x % 3 == 0 and x % 5 == 0:
        print(x)


check(a)
check(b)
check(c)
check(d)