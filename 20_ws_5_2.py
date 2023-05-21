num = input ("Enter any integer: ")
total=0
for i in range(3,len(num)):
    x=int(num[i])
    total+=x


print ("The sum of the digits is", total)