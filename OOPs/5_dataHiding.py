class Abc:
    def __init__(self):
        self.__a = 1
    def disp(self):
        return self.__a
    def __disp2(self):
        print("By __disp2")
        return self.__a
    
    def disp3(self):
        return self.__disp2()


obj1 = Abc()

print(obj1.disp3())