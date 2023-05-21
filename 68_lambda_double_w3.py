def multi(n):
    return lambda a : a * n


mydoubler = multi(2)
mytripler = multi(3)

print(mydoubler(11))
print(mytripler(11))