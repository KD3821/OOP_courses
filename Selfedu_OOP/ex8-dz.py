
class AMD:
    def __init__(self):
        print(f"Конструктор AMD")
        super().__init__()


class Intell:
    def __init__(self):
        print(f"Конструктор Intell")
        super().__init__()


class NVidia:
    def __init__(self):
        print(f"Конструктор NVidia")
        super().__init__()


class GeForce:
    def __init__(self):
        print(f"Конструктор GeForce")
        super().__init__()


class Memory:
    def __init__(self):
        print(f"Конструктор Memory")
        super().__init__()

class ViewSonic:
    def __init__(self):
        print(f"Конструктор ViewSonic")
        super().__init__()

class Dell:
    def __init__(self):
        print(f"Конструктор Dell")
        super().__init__()

class Monitor(ViewSonic, Dell):
    def __init__(self, screen1: ViewSonic = None, screen2: Dell = None):
        self.screen1 = screen1
        self.screen2 = screen2
        print(f"Конструктор Monitor")
        super().__init__()


    def getMonitor(self):
        if self._screen1 is None:
            print(f"Установлен Монитор: {self._screen2.__name__}")
        elif self._screen2 is None:
            print(f"Установлен Монитор: {self._screen1.__name__}")
        else:
            print("Отсутствует Монитор!!!")


class CPU(AMD, Intell):
    def __init__(self, proc1: AMD = None, proc2: Intell = None):
        self.proc1 = proc1
        self.proc2 = proc2
        print(f"Конструктор CPU")
        super().__init__()


    def getCPU(self):
        if self._proc1 is None:
            print(f"Процессор: {self._proc2.__name__}")
        elif self._proc2 is None:
            print(f"Процессор: {self._proc1.__name__}")
        else:
            print("Сбой работы Процессора!!!")

    # def getCPU(self, proc1: AMD = None, proc2: Intell = None):
    #     if proc1 is None:
    #         print(f"Процессор: {self.proc2}")
    #     elif proc2 is None:
    #         print(f"Процессор: {self.proc1}")
    #     else:
    #         print("Сбой работы Процессора!!!")


class GPU(NVidia, GeForce):
    def __init__(self, vid1: NVidia = None, vid2: GeForce = None):
        self.vid1 = vid1
        self.vid2 = vid2
        print(f"Конструктор GPU")
        super().__init__()

    def getGPU(self):
        if self._vid1 is None:
            print(f"Видеокарта: {self._vid2.__name__}")
        elif self._vid2 is None:
            print(f"Видеокарта: {self._vid1.__name__}")
        else:
            print("Сбой работы Видеокарты!!!")


class Motherboard(CPU, GPU, Memory, Monitor):
    def __init__(self, cpu: CPU, gpu: GPU, mem: Memory, screen: Monitor):
        print(f"Конструктор Motherboard")
        self._proc1 = cpu
        self._proc2 = None
        self._vid1 = gpu
        self._vid2 = None
        self._mem = mem
        self._screen1 = screen
        self._screen2 = None
        super().__init__()

    def showInfo(self):
        print(f"Материнская плата:\nПамять: {self._mem}")
        self.getCPU()
        self.getGPU()
        self.getMonitor()




m = Motherboard(AMD, NVidia, '160Gb', Dell)
m.showInfo()
print("___")
CPU.getCPU(m)
# print(dir(Motherboard))
#
# sc = Monitor(Dell)
# sc.__getMonitor()
