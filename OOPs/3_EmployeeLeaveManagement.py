class Employee:
    salPerDay = 1200

    def __init__(self, name, leave):
        # salPerDay = 1200
        self.name = name
        self.leave = leave

    def showData(self):
        self.salary = self.salPerDay * (30 - self.leave)
        print("Salary of", self.name, ":", self.salary, ", and leave:", self.leave)


emp1 = Employee("Rahul", 3)
emp1.showData()

emp2 = Employee("Abhi", 5)
emp2.showData()

print("\n\nBY USING FOR LOOP")

l = []
no = int(input("Numbers of employee is: "))

for i in range(no):
    name = input("name: ")
    leave = int(input("leave: "))
    l.append(Employee(name, leave))
    l[i].showData()
