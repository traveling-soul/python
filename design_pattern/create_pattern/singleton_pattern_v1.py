def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton

@Singleton
class A:
    a = 1

    def __init__(self, x=0):
        self.x = x


if __name__ == '__main__':
    a1 = A(2)
    a2 = A(3)
    print(a1 is a2)
    print(a1.x, a2.x)