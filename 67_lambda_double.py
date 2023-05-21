n = int(input("n: "))

doub = lambda a : a * 2

print(doub(n))

print("\n\nArea of triangle using lambda function")

radius = float(input("Enter radius: "))

area = lambda r : 3.14 * (r ** 2)

print(format(area(radius), '.2f'))