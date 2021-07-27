class Rectangle:
    __square = 0

    def __init__(self, x = 0, y = 0):
        self.__a = x
        self.__b = y
        Rectangle.__square = self.__a * self.__b

    @staticmethod
    def getSquare():
        return Rectangle.__square


rec = Rectangle(5,5)
print(rec.getSquare())
rec1 = Rectangle(10,5)
print(rec1.getSquare())
rec2 = Rectangle(2.5,4)
print(rec2.getSquare())