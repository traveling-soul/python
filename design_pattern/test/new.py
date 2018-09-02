class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        cls._state = ob.__dict__
        return cls


class MyClass2(Borg):
    a = 1


obj = MyClass2()
obj2 = MyClass2()
print(obj is obj2)
print(obj == obj2)