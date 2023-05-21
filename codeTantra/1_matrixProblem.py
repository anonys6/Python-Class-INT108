k = 1

p = [[0 for x in range(50)] for y in range(50)]
q = [[0 for x in range(50)] for y in range(50)]
r = [[0 for x in range(50)] for y in range(50)]

ct = 0
R = 1


def read(a, r, c, C, R):
    k = 1
    R = 1
    ct = 0

    print("Enter the matrix:")
    for i in range(0, r):
        for j in range(0, r):
            num = int(input())
            if (num != 0):
                a[R][C] = i
                c += 1
                a[R][C] = j
                ct += 1
                a[R][C] = num
                ct += 1
                R += 1
                C = 0
    a[0][0] = r
    a[0][1] = c
    a[0][2] = ct
    print("Sparse Matrix in memory:")
    for i in range(0, ct + 1):
        for j in range(0, 3):
            print(a[i][j], end=" ")
        print()


def transpose():
    print("Enter the row & column of 1st matrix: ")
    r1 = int(input())
    c1 = int(input())
    read(p, r1, c1, 0, 0)
    print("TRANSPOSE: ")
    k = 1

    # write your code here


ct = 0
transpose()
