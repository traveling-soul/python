"""
用列表模拟双端队列，列表为0的位置表示队尾，列表为-1的位置表示队首
双端队列在两端既可以进行添加操作，也可以进行删除操作
"""

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # 队尾添加元素
    def addRear(self, item):
        self.items.insert(0, item)

    # 队首添加元素
    def addFront(self, item):
        self.items.append(item)

    # 队尾删除元素
    def removeRear(self):
        self.items.pop(0)

    # 队首添加元素
    def removeFront(self):
        self.items.pop()

    def size(self):
        return len(self.items)