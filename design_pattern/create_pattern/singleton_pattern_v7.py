class Singleton(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Singleton, cls).__new__(cls, *args, **kwargs)
        cls._state = obj.__dict__
        return cls


class Myclass(Singleton):
    a = 1


if __name__ == '__main__':
    obj = Myclass()
    obj2 = Myclass()
    print(obj is obj2)