class CoordValue:
    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        self.__value = value

    def __delete__(self, obj):
        del self.__value


class Point:
    coordX = CoordValue()
    coordY = CoordValue()

    def __init__(self, x = 0, y = 0):
        self.coordX = x
        self.coordY = y
    #     self.__x = x
    #     self.__y = y
    #     print("Создали экземпляр")
    #
    # def __checkValue(x):
    #     if isinstance(x, int) or isinstance(x, float):
    #         return True
    #     return False
    # @property
    # def coordX(self):
    #     print("вызов __getCoordX")
    #     return self.__x
    # @coordX.setter
    # def coordX(self, x):
    #     if Point.__checkValue(x):
    #         print("вызов __setCoordX")
    #         self.__x = x
    #     else:
    #         raise ValueError("Неверный формат данных")
    # @coordX.deleter
    # def coordX(self):
    #     print("Удаление свойства")
    #     del self.__x


    # coordX = property(__getCoordX, __setCoordX, __delCoordX)

pt = Point(1, 2)
# print(pt.coordX)
# pt.coordX = 100
# a = pt.coordX
# print(a)
# del pt.coordX
# print(a)
# print(pt)
pt.coordX = 5
print(pt.coordX, pt.coordY)