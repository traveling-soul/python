# import threading
#
# class SingletonType(type):
#     _instance_lock = threading.Lock()
#     def __call__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             with SingletonType._instance_lock:
#                 if not hasattr(cls, "_instance"):
#                     cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
#         return cls._instance
#
# class Foo(metaclass=SingletonType):
#     def __init__(self,name):
#         self.name = name
#
#
# obj1 = Foo('name')
# obj2 = Foo('name')
# print(obj1,obj2)


# 共享属性，__dict__
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