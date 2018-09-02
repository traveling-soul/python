import time
import threading

class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


def task(arg):
    obj = Singleton()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task, args=[i,])
    t.start()
time.sleep(20)
obj = Singleton.instance()
print(obj)