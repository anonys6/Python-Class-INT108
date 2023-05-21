num = int(input("Enter a number: "))
numClone = num

rev = 0

while (num != 0):
    rem = num % 10
    num = num // 10
    rev = rev * 10 + rem
    if numClone == rev:
        print(rev,"number is a pallendrom number")

# numQ = num // 10
# numR = num % 10
