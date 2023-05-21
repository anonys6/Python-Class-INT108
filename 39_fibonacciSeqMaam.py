num1 = 0
num2 = 1
sumPreviousTwo = 0
last = int(input("Enter last number: "))
while (num1 + num2) < last:
    sumPreviousTwo = num1 + num2
    print(sumPreviousTwo, end=",")
    num1 = num2
    num2 = sumPreviousTwo
