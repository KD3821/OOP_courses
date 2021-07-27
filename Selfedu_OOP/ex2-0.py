class Point():
    def __init__(self, x=1, y=2):
        self.a = x
        self.b = y
        print("Создание экземпляра класса Point")

    def setCoords(self, m=2, n=3):
        self.s = m
        self.t = n

    def __del__(self):
        print("Удаление" +self.__str__())



print("создаем экземпляр класса без аргументов")
pt = Point()
print(getattr(pt, "x", False))
print(getattr(pt, "y", False))
print(getattr(pt, "a", False))
print(getattr(pt, "b", False))
print(pt.__dict__)
print("создаем другой экземпляр класса c аргументам 5 и 10")
pt1 = Point(5,10)
print(getattr(pt1, "x", False))
print(getattr(pt1, "y", False))
print(getattr(pt1, "a", False))
print(getattr(pt1, "b", False))
print(pt1.__dict__)
print("вызываем метод setCoords без аргументов")
pt.setCoords()
print(getattr(pt, "m", False))
print(getattr(pt, "n", False))
print(getattr(pt, "s", False))
print(getattr(pt, "t", False))
print(pt.__dict__)
print("вызываем метод setCoords с аргументами 5 и 25")
pt.setCoords( 5, 25)
print(getattr(pt, "m", False))
print(getattr(pt, "n", False))
print(getattr(pt, "s", False))
print(getattr(pt, "t", False))
print(pt.__dict__)
print("У другого экземпляра вызываем метод setCoords с аргументами 5 и 25")
pt1.setCoords( 5, 25)
print(getattr(pt1, "m", False))
print(getattr(pt1, "n", False))
print(getattr(pt1, "s", False))
print(getattr(pt1, "t", False))
print(pt1.__dict__)
pt=2
pt=22