a = (2, 4, 6, 8)        # table of 2
b = (4, 8, 12, 16)      # table of 4
c = (2, 4, 6, 8)        # natural even number

def compTup (a, b):
    for i in a:
        if a[i] != b[i]:
            return False
        else:
            a = True
        return a


print(compTup(a, b))
print(compTup(a, c))