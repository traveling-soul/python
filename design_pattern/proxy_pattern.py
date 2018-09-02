"""
代理者模式中，代理者隐藏了真实的对象，代理者和真实对象需要实现相同的方法，可通过接口编程
"""

from abc import ABCMeta, abstractmethod


class GiveGift(ABCMeta):
    @abstractmethod
    def give_dolls(self):
        pass

    @abstractmethod
    def give_flowers(self):
        pass

    @abstractmethod
    def give_chocolate(self):
        pass


class Pursuit(GiveGift):
    girl = None

    def __init__(self, girl):
        self.girl = girl

    def give_dolls(self):
        print('送你洋娃娃')

    def give_flowers(self):
        print('送你鲜花')

    def give_chocolate(self):
        print('送你巧克力')


class Proxy(GiveGift):
    def __init__(self, girl):
        self.pursuit = Pursuit(girl)

    def give_dolls(self):
        self.pursuit.give_dolls()

    def give_flowers(self):
        self.pursuit.give_flowers()

    def give_chocolate(self):
        self.pursuit.give_chocolate()


class Girl:
    _name = None

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


if __name__ == '__main__':
    girl = Girl()
    girl.name = '李娇娇'

    proxy = Proxy(girl)

    proxy.give_dolls()
    proxy.give_flowers()
    proxy.give_chocolate()



