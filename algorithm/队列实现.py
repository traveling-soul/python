"""
用列表模拟队列，列表下标为0的位置表示队尾，下标为-1的位置表示队首，先进先出（FIFO）
"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # 入队
    def enqueue(self, item):
        self.items.insert(0, item)

    # 出队
    def dequeue(self):
        return self.items.pop()

    # 返回队列的长度
    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q.isEmpty())
    q.enqueue(8.4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())


