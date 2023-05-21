# FIBONACCI USING RECURSION

def fibo (n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n - 2)


n = int(input("How many terms: "))

if n <= 0:
    print("Please enter positive integer")
else:
    print("Fibonacci Sequence")
    for i in range(n):
        print(fibo(i))



        
        