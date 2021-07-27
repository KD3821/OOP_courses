class Point():
    x = 1; y = 1
    def __init__(self, x=4, y=5):
        self.x = x
        self.y = y
        print("Создание экземпляра класса Point")

    def setCoords(self, a=2, b=3):
        self.m = a
        self.n = b

pt = Point()
print(getattr(pt, "x", False))
print(getattr(pt, "y", False))
# print(getattr(pt, "xx", False))
# print(getattr(pt, "yy", False))
print(getattr(pt, "m", False))
print(getattr(pt, "n", False))
print(pt.__dict__)
print("вызываем метод setCoords без аргументов")
pt.setCoords()
print(getattr(pt, "x", False))
print(getattr(pt, "y", False))
# print(getattr(pt, "xx", False))
# print(getattr(pt, "yy", False))
print(getattr(pt, "m", False))
print(getattr(pt, "n", False))
print(pt.__dict__)
print("вызываем метод setCoords с аргументами 5 и 25")
pt.setCoords( 5, 25)
print(getattr(pt, "x", False))
print(getattr(pt, "y", False))
# print(getattr(pt, "xx", False))
# print(getattr(pt, "yy", False))
print(getattr(pt, "m", False))
print(getattr(pt, "n", False))
print(pt.__dict__)
# pt.x = 5
# pt.y = 10
# pt.setCoords()
#
# pt1 = Point()
# pt2 = Point()
