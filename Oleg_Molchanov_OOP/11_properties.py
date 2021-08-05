

class Person:
    def __init__(self, name):
        self._name = name

    # def get_name(self):                               #first-second-third try
    #     print('From get_name()')
    #     return self._name
    #
    # def set_name(self, value):
    #     print('From set_name()')
    #     self._name = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    # name = property(fget=get_name, fset=set_name)     # first try

    # name = property()                                 #second try
    # name = name.getter(get_name)
    # name = name.setter(set_name)

    # name = property(get_name)                         #third try
    # name = name.setter(set_name)


p = Person('Dima')