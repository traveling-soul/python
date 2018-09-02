from abc import ABCMeta, abstractmethod


# 产品类
class AbstractBuilder(metaclass=ABCMeta):
    @abstractmethod
    def add_a(self):
        pass

    @abstractmethod
    def add_b(self):
        pass


class BuilderA(AbstractBuilder):
    def __init__(self):
        self.product = []

    def add_a(self):
        self.product.append('a_a')

    def add_b(self):
        self.product.append('a_b')

    def __str__(self):
        result = '产品A：'
        for i in self.product:
            result += i + " "
        return result


class BuilderB(AbstractBuilder):
    def __init__(self):
        self.product = []

    def add_a(self):
        self.product.append('b_a')

    def add_b(self):
        self.product.append('b_b')

    def __str__(self):
        result = '产品B：'
        for i in self.product:
            result += i + " "
        return result


def director(builder):
    builder.add_a()
    builder.add_b()


def main():
    builder_a = BuilderA()
    builder_b = BuilderB()

    director(builder_a)
    print(builder_a)
    director(builder_b)
    print(builder_b)


main()