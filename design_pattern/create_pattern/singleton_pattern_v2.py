import time

class Singleton:
    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance


# single1 = Singleton.instance()
# single2 = Singleton.instance()
# print(single1 is single2)


import threading

def task(arg):
    obj = Singleton.instance()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task, args=[i,])
    t.start()
