"""
用列表模拟栈，列表下标为0的位置表示底部，下标为-1的位置表示顶部，后进先出（LIFO）
"""

# class Stack:
#     # 初始化
#     def __init__(self):
#         self.items = []
#
#     # 判断是否为空
#     def isEmpty(self):
#         return self.items == []
#
#     # 进栈
#     def push(self, item):
#         self.items.append(item)
#
#     # 出栈
#     def pop(self):
#         return self.items.pop()
#
#     # 返回栈顶元素
#     def peek(self):
#         return self.items[len(self.items)-1]
#
#     # 返回栈的大小
#     def size(self):
#         return len(self.items)


if __name__ == '__main__':
    from pythonds.basic.stack import Stack

    s = Stack()
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())