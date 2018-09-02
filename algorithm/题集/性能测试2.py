def f1(lln):
    l1 = sorted(lln)
    l2 = [i for i in l1 if i < 0.5]
    return [i*i for i in l2]


def f2(lln):
    l1 = [i for i in lln if i < 0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]


def f3(lln):
    l1 = [i*i for i in lln]
    l2 = sorted(l1)
    return [i for i in l2 if i < (0.5*0.5)]


import cProfile
import random

lln = [random.random() for i in range(100000)]
cProfile.run('f1(lln)')
cProfile.run('f2(lln)')
cProfile.run('f3(lln)')


