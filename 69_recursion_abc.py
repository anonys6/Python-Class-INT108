def abc (a, b):
    if a < b * 2:
        abc(a-1, b-1)
        print("a:", a)
        print("b:", b)
    print("outer a:", a)
    print("outer b:", b)


abc(5, 4)