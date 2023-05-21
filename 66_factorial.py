# FACTORIAL OF A NUMBER USING RECURSION

def fact(x):
    if x == 0 or x == 1:
        return 1
    return x * fact(x - 1)


n = int(input("n: "))

print(fact(n))


