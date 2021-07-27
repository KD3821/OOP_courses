class Clock:
    __DAY = 86400

    def __init__(self, secs:int):
        if not isinstance(secs, int):
            raise ValueError("Секунды должны быть целым числом")
        self.__secs = secs % self.__DAY

    def getFormatTime(self):
        s = self.__secs % 60             # seconds
        m = (self.__secs // 60) % 60     # minutes
        h = (self.__secs // 3600) % 24   # hours
        return f"{Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)}"

    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else "0"+str(x)

    def getSeconds(self):
        return self.__secs

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.__secs + other.getSeconds())

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        self.__secs += other.getSeconds()
        return self

    def __eq__(self, other):
        # if self.__secs == other.getSeconds():
        #     return True
        # return False
        return self.__secs == other.getSeconds()

    def __nq__(self, other):
        return not self.__eq__(other)


    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")
        if item == "hour":
            return (self.__secs // 3600) % 24
        elif item == "min":
            return (self.__secs // 60) % 60
        elif item == "sec":
            return (self.__secs % 60)

        return "Неверный ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")
        if not isinstance(value, int):
            raise ValueError("Значение должно быть целым числом")

        s = self.__secs % 60  # seconds
        m = (self.__secs // 60) % 60  # minutes
        h = (self.__secs // 3600) % 24  # hours

        if key == "hour":
            self.__secs = s + 60 * m + value * 3600
        elif key == "min":
            self.__secs = s + 60 * value + h * 3600
        elif key == "sec":
            self.__secs = value + 60 * m + h * 3600




c1 = Clock(8000)
c2 = Clock(3000)
c3 = c1 + c2
c4 = c1 + c2 + c3

print(c1.getFormatTime())
print(c2.getFormatTime())
print(c3.getFormatTime())
print(c4.getFormatTime())
c1 += c4
print(c1.getFormatTime())
c2 += c3 + c4
print(c2.getFormatTime())

if c1 == c2:
    print("времена равны")
else:
    print("not equal")

if c1 != c2:
    print("времена неравны")


print(c2.getFormatTime())
print(c2["hour"], c2["min"], c2["sec"])
c2["hour"] = 23
print(c2["hour"], c2["min"], c2["sec"])
print(c2.getFormatTime())
