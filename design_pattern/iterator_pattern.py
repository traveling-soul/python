from abc import ABCMeta, abstractmethod


class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def is_done(self):
        pass

    @abstractmethod
    def current_item(self):
        pass


class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def create_iterator(self):
        pass


class ConcreteIterator(Iterator):
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.current = 0

    def first(self):
        return self.aggregate[0]

    def next(self):
        ret = None
        self.current += 1
        if self.current < self.aggregate.get_count():
            ret = self.aggregate[self.current]
            return ret

    def is_done(self):
        return True if self.current >= self.aggregate.get_count() else False

    def current_item(self):
        return self.aggregate[self.current]


class ConcreteAggregate(Aggregate):
    def __init__(self):
        self.items = []
        self.count = 0

    def create_iterator(self):
        return ConcreteIterator(self)

    def get_count(self):
        self.count =len(self.items)
        return self.count

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items.insert(index, value)


if __name__ == '__main__':
    aggregate = ConcreteAggregate()

    aggregate[0] = '大鸟'
    aggregate[1] = '小菜'
    aggregate[2] = '行李'
    aggregate[3] = '老外'
    aggregate[4] = '公交内部员工'
    aggregate[5] = '小偷'

    iterator = ConcreteIterator(aggregate)
    item = iterator.first()
    # print(item)
    while not iterator.is_done():
        print('{0} 请买车票！'.format(iterator.current_item()))
        iterator.next()

    # for a in aggregate:
    #     print(a)
    #
    # print(aggregate[2:5])




