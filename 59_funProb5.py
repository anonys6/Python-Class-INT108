def pyramid (x):
    for i in range(0, x):
        for j in range(1, i + 1):
            print("*", end=" ")

        print()


pyramid(5)