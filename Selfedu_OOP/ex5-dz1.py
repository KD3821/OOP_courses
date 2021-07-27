class Dog:
    __count = 0
    __instance = None


    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__instance = super(Dog, cls).__new__(cls)
            print("Завели собаку!")
            print(cls.__instance)
            return cls.__instance
        else:
            print("Слишком много развелось собак!")
            cls.__instance = None
            print(cls.__instance)
            print(id(cls.__instance))


    def __init__(self, name='.', age=0, breed='.'):
        print("ok")
        Dog.__count += 1
        self.name = name
        self.age = age
        self.breed = breed

    def getID(self):
        print(id(self.__instance))

    # @staticmethod
    # def getCount():
    #     return Dog.__count


dog = Dog('A', 5, "yt")
print(dog.name, dog.age, dog.breed)
Dog.getID(dog)
dog2 = Dog('B', 2, "gs")
print(dog2.name, dog2.age, dog2.breed)
Dog.getID(dog)
dog3 = Dog('C', 10, "bu")
print(dog3.name, dog3.age, dog3.breed)
Dog.getID(dog)
dog4 = Dog('D', 4, "la")
print(dog4.name, dog4.age, dog4.breed)
Dog.getID(dog)
dog5 = Dog('E', 3, "ch")
print(dog5.name, dog5.age, dog5.breed)
Dog.getID(dog)
dog6 = Dog('F', 1, "bi")
# print(dog6.name, dog6.age, dog6.breed)
Dog.getID(dog)
dog7 = Dog('G', 15, "bu")
# print(dog7.name, dog7.age, dog7.breed)
Dog.getID(dog)
print('_________')
print(id(dog), id(dog2), id(dog3), id(dog4), id(dog5), id(dog6), id(dog7), sep="\n")