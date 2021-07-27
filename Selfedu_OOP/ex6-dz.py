class PersComp:
    def __init__(self, ddr = 0, hdd = 0, model = 0, cpu = 0):
        print("Конструктор базового класса PersComp")
        self._ddr = ddr
        self._hdd = hdd
        self._model = model
        self._cpu = cpu

    def getInfo(self):
        return self._ddr, self._hdd, self._model, self._cpu


class Desktop(PersComp):
    def getTechs(self, a=0, b=0, c=0, d=0, f=0, g=0):
        self._monitor = a
        self._keyboard = b
        self._mouse = c
        self._length = d
        self._width = f
        self._high = g
        print(f"НастКомпютер: {self._monitor}, {self._keyboard}, {self._mouse}, {self._length}, {self._width}, {self._high}, {self.getInfo()}")



class Laptop(PersComp):
    def __init__(self, *args):
        print("переопределенный конструктор Laptop")
        super().__init__(*args)

    def getTechs(self, a=0, b=0, c=0, d=0):
        self._length = a
        self._width = b
        self._high = c
        self._screen = d
        print(f"ноутбук: {self._length}, {self._width}, {self._high}, {self._screen}, {self.getInfo()}")


d = Desktop(3, 160, 8, 1.6)
l = Laptop(4, 80, 6, 2.2)

print(d._ddr)
print(l._ddr)
#
print(d.getInfo())
print(l.getInfo())

d.getTechs(1, 2, 3, 4, 5, 6)
l.getTechs(7, 8, 9, 10)



