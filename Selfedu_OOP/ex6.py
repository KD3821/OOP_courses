class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x},{self.__y})"

class Prop:
    def __init__(self, sp:Point, ep:Point, color:str = "red", width:int = 1 ):
        print("Конструктор базового класса Prop")
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width

    def getWidth(self):
        return self.__width


class Line(Prop):
    def __init__(self, *args):
        print("Переопределенный конструктор Line")
        # Prop.__init__(self, *args)
        super().__init__(*args)
        self.__width = 5

    # def __init__(self, sp:Point, ep:Point, color:str = "red", width:int = 1 ):
    #     self._sp = sp
    #     self._ep = ep
    #     self._color = color
    #     self._width = width

    def drawLine(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.__width}")


class Rect(Prop):
    # def __init__(self, sp:Point, ep:Point, color:str = "red", width:int = 1 ):
    #     self._sp = sp
    #     self._ep = ep
    #     self._color = color
    #     self._width = width

    def drawRect(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")



l = Line( Point(1,2), Point(10,20) )
l.drawLine()
r = Rect( Point(30,40), Point(70,80))
r.drawRect()

# print(l._width)
print(l.__dict__)