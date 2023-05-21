x0 = int (input ("Enter the coordinate of x0: "))
y0 = int (input ("Enter the coordinate of y0: "))
x1 = int (input ("Enter the coordinate of x1: "))
y1 = int (input ("Enter the coordinate of y1: "))

dist = (((x0 - x1)**2) + ((y0 - y1)**2))

print ("The distance between coordinate (", x0, ",", y0, ") and (", x1, ",", y1, ") is: ", dist)