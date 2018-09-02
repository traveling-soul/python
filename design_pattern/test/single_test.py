class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance


class MyClass(Singleton):
    a = 1


obj = MyClass()
obj2 = MyClass()
print(obj is obj2)
