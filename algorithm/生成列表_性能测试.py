from timeit import Timer


def test1():
    ls = []
    for i in range(1000):
        ls = ls + [i]


def test2():
    ls = []
    for i in range(1000):
        ls.append(i)


def test3():
    ls = [i for i in range(1000)]


def test4():
    ls = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "millionseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")