class Parent:
    def number(self, n):
        if n == 0:
            print("Zero")
        isPositive = False
        if n >= 0:
            isPositive = True
        x = 2 ** 5
        if x == n or -x == n:
            if isPositive:
                print(f"positive and perfect")
            else:
                print(f"negative and perfect")
        else:
            if isPositive:
                print(f"positive and Nonperfect")
            else:
                print(f"negative and Nonperfect")

class Child(Parent):
    def number(self, n):
        if n == 0:
            print("Zero")
            return
        isPositive = False
        if n >= 0:
            isPositive = True
        x = 2 ** 5
        if x == n or -x == n:
            if isPositive:
                print(f"positive and perfect")
            else:
                print(f"negative and perfect")
        else:
            if isPositive:
                print(f"positive and Nonperfect")
            else:
                print(f"negative and Nonperfect")

a = Child()
num = int(input())
a.number(num)