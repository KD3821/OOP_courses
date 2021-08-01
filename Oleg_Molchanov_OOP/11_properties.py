

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, value):
        print('From set_name()')
        self._name = value

    name = property(fget=get_name, fset=set_name)

p = Person('Dima')