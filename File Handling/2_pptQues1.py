f = open("File Handling/personalDetails.txt", "w")
f.write("Name: Md Shakib Alam\n")
f.write("Course: CSE\n")
f.write("Address: JH, India\n")
f.close()

f = open("File Handling/personalDetails.txt", "r")
print(f.read())
f.close()