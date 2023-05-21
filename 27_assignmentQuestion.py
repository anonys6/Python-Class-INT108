from string import *
fullString = input("Enter full string: ")
subString = input("Enter sub string: ")
if(subString in fullString):
    print(subString.capitalize())
else:
    print("Substring is not a part of string")
