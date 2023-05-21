def isPrime(n):
    if(n==2):
        return True
    if(n < 2 or n%2==0):
        return False
    for i in range(3,int(n**(0.5))+1):
        if(n%i==0):
            return False
    return True

n = int(input())
liss = []
for i in range(1,n+1):
    if(isPrime(i)):
        liss.append(i**2)
print(liss)