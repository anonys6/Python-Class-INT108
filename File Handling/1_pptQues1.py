f = open("File Handling/test.txt", "r")
# f.write("Now is the time")
# f.write(" changing file text")
# print(f.readline())
# print(f.readline())
for i in f:
    print(i, end="")
f.close()