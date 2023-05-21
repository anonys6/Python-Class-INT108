class student:
    def __init__(self, name, age, section = "k22ep"):
        self.name = name
        self.age = age
        self.section = section
    
    def show(self):
        print(self.name, end=", ")
        print(self.age, end=", ")
        print(self.section)


s1 = student("amit", 39)
s2 = student("amit", 39)
s3 = student("amit", 39)
s4 = student("amit", 39)
s5 = student("abhi", 29, "k23ek")

s1.show()
s2.show()
s3.show()
s4.show()
s5.show()


# ANOTHER METHOD USING FOR LOOP 


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def showData(self):
        print("name:", self.name, ", age:", self.age)


l = []
no = int(input("Total number of students: "))

for i in range(no):
    name = input("name: ")
    age = input("age: ")
    l.append(Employee(name, age))
    l[i].showData()