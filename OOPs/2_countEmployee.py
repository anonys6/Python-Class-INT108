class Employee:
    count = 0
    def __init__(self):
        Employee.count += 1
    
    def showEmp(self):
        print(Employee.count)



s1 = Employee()
s2 = Employee()
s4 = Employee()
s4 = Employee()

s4.showEmp()

print("by using member variable:", s4.count)