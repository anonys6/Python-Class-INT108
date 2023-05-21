age = int(input("Enter your age: "))

if age > 18:
    print("You can access the file")
    f = open("File Handling/personalDetails.txt", "r")
    print(f.read())
    f.close()
else:
    print("You can't access the data")