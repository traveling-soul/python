"""
孩子们围成一个圈，并尽可能快的将一个
山芋递给旁边的孩子。在某一个时间，动作结束，有山芋的孩子从圈中移除。游戏继续开始
直到剩下最后一个孩子。
"""
from pythonds.basic.queue import Queue


def hotPotato(namelist, num):
    simque = Queue()
    for name in namelist:
        simque.enqueue(name)

    while simque.size() > 1:
        for i in range(num):
            simque.enqueue(simque.dequeue())
        simque.dequeue()
    return simque.dequeue()

print(hotPotato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))