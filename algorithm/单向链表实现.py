# 节点类
class SingleNode:
    def __init__(self, item):
        # 信息域：存储节点数据
        self.item = item
        # 链接域：链接下一个节点
        self.next = None


# 单向链表
class SingleLinkList:
    def __init__(self):
        # head：头节点的引用
        self._head = None

    # 链表是否为空
    def is_empty(self):
        return self._head is None

    # 链表长度
    def length(self):
        count = 0
        # cur指向链表的首节点
        cur = self._head
        while cur is not None:
            # cur不等于None，就表示一个节点存在
            # 给计数器加1
            count += 1
            # cur指向当前节点的下一个节点
            cur = cur.next
        return count

    # 遍历
    def travel(self):
        # cur指向链表的首节点
        cur = self._head
        while cur is not None:
            # 打印当前节点的数据
            print(cur.item)
            # cur指向下一个节点
            cur = cur.next

    # 链表头部添加元素
    def add(self, item):
        # 生成新的节点对象
        node = SingleNode(item)
        # 设置node节点的next指向原来的头节点
        node.next = self._head
        # 把node节点设置成新的头节点
        self._head = node

    # 链表尾部添加元素
    def append(self, item):
        # 定义新的节点对象
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            # cur指向链表的开头
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            # cur是链表的最后一个节点
            cur.next = node

    # 指定位置添加元素
    def insert(self, pos, item):
        if pos <= 0:
            # 在链表的头部添加节点
            self.add(item)
        elif pos >= self.length():
            # 在链表的尾部添加节点
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            cur = self._head
            while count < pos - 1:
                count += 1
                cur = cur.next
            # 插入操作
            node.next = cur.next
            cur.next = node

    # 删除节点
    def remove(self, item):
        cur = self._head
        # pre：保存cur的上一个节点
        pre = None
        while cur is not None:
            if cur.item == item:
                # 确定要删除的节点
                if not pre: # pre == None:
                    # 删除的是第一个节点
                    # 把当前节点的下一个节点当作首节点
                    self._head = cur.next
                else:
                    # 删除的不是第一个节点
                    pre.next = cur.next
                break
            else:
                # 不相等，不是要删除的节点
                # 遍历下一个节点
                pre = cur
                cur = cur.next

    # 查找节点
    def search(self, item):
        # 寻找节点是否存在
        cur = self._head
        while cur != None:
            # 判定是不是要查找的节点
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    sl = SingleLinkList()
    sl.add(1)
    sl.add(2)
    sl.append(3)
    sl.insert(2, 6)
    print('length:', sl.length())
    sl.travel()
    print(sl.search(2))
    sl.remove(2)
    print('length:', sl.length())


