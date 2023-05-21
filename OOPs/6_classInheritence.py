class Parent:
    def __init__(self):
        print("Parent constructor")
        self.a = 1
    
    def disp(self):
        print("Parent disp method")
        self.a += 1
        print(self.a)
    

class Child(Parent):
    def dispChild(self):
        print("I am a child class")


c1 = Child()

c1.disp()
c1.dispChild()

p1 = Parent()

p1.disp()
p1.dispChild()