def recEven (a):
    if a % 2 == 0:
        recEven(a - 2)
        print("inner a:", a)
    print("outer a:", a)


recEven(10)