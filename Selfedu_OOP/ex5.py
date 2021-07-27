class Point:
    __count = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(Point, cls).__new__(cls)
            print(cls.__instance)
        else:
            print("Экземпляр класса Point уже создан!")


    def __init__(self, x = 0, y = 0):
        Point.__count += 1
        print("test")
        self.coordX = x
        self.coordY = y

    @staticmethod
    def getCount():
        return Point.__count

def getCount():
    return 5

pt = Point()
pt2 = Point()
pt3 = Point()
print(id(pt), id(pt2), id(pt3), sep="\n")
# print(pt.getCount(), Point.getCount())
# pt.getCount = getCount
# print(pt.getCount(), Point.getCount())
