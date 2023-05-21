class A:
    def __init__(self, sinChar):
        self.sinChar = sinChar

    def char(self):
        return self.sinChar.lower()


class B(A):
    def __init__(self, newChar):
        self.newChar = newChar

    def char(self):
        return ord(self.newChar)

    def char1(self):
        return self.newChar.upper()


char = input()

objA = A(char)
objB = B(char)

if len(char) == 1 and char.isalpha():
    print(objA.char())
    print(objB.char())
    print(objB.char1())
else:
    print("Invalid")
    print(objB.char())