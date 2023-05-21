s1 = float(input("Enter first side: "))
s2 = float(input("Enter second side: "))
s3 = float(input("Enter third side: "))

if s1 == s2 == s3:
    print("Equilateral triangle")
elif s1 != s2 and s2 != s3:
    print("Scalene triangle")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles triangle")