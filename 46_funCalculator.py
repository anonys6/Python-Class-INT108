def add (x, y):
    print("Addition")
    c = x + y
    print(x, "+", y, "=", c)


def subtract (x, y):
    print("Subtraction")
    c = x - y
    print(x, "-", y, "=", c)


def multiply (x, y):
    print("Multiply")
    c = x * y
    print(x, "*", y, "=", c)


def division (x, y):
    print("Division")
    c = x / y
    print(x, "/", y, "=", c)


opera = input("Which operation you want to do:\nPress 1, 2, 3 and 4 for addition, subtraction, multiplication and "
              "division respectively: ")
a = int(input("Enter first operand: "))
b = int(input("Enter second operand: "))

while (1):
    if opera == "1":
        add(a, b)
    elif opera == "2":
        subtract(a, b)
    elif opera == "3":
        multiply(a, b)
    elif opera == "4":
        division(a, b)
    else:
        print("ERROR: You entered invalid operator")
        break

