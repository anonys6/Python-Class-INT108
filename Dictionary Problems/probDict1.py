myDict = {}

terms = int(input("How many terms you want in dictionary to contain: "))

for i in range (0, terms):
    myDict[i]  = input()


print(myDict)