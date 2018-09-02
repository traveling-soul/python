"""
中介者模式避免了各个对象之间的直接交互，降低了耦合。
各个对象互相不认识，但都认识中介者，中介者需要认识各个对象。
中介者模式将各个对象交互的网状结构变成了以中介者为中心的集中式结构。
"""

from abc import ABCMeta, abstractmethod


# 联合国机构
class UnitedNations(metaclass=ABCMeta):
    @abstractmethod
    def declare(self, message, colleague):
        pass


class Country(metaclass=ABCMeta):
    def __init__(self, mediator):
        self.mediator = mediator


class USA(Country):
    def declare(self, message):
        self.mediator.declare(message, self)

    def get_message(self, message):
        print('美国获得对方信息：', message)


class Iraq(Country):
    def declare(self, message):
        self.mediator.declare(message, self)

    def get_message(self, message):
        print('伊拉克获得对方信息：', message)


# 联合国安全理事会
class UnitedNationsSecurityCouncil(UnitedNations):
    def __init__(self):
        self.colleague1 = None
        self.colleague2 = None

    def declare(self, message, colleague):
        if colleague == self.colleague1:
            self.colleague2.get_message(message)
        else:
            self.colleague1.get_message(message)


def main():
    unsc = UnitedNationsSecurityCouncil()
    # 让各个国家认识联合国
    usa = USA(unsc)
    iraq = Iraq(unsc)

    # 让联合国认识各个国家
    unsc.colleague1 = usa
    unsc.colleague2 = iraq

    usa.declare('不准研究核武器，否则要发动战争！')
    iraq.declare('我们没有核武器，也不怕侵略。')


main()

