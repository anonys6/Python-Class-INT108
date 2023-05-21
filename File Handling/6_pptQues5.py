printTill = int(input("How much you want to print: "))

f = open("File Handling/story21.txt", "r")
print(f.read(printTill))
f.close()