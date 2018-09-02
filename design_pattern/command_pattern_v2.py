from abc import abstractmethod, ABCMeta
from datetime import datetime


class Command(metaclass=ABCMeta):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def executeCommand(self):
        pass


class BakeMuttonCommand(Command):
    def executeCommand(self):
        self.receiver.bakeMutton()

    def __str__(self):
        return '命令模式.烤羊肉串'


class BakeChickenWingCommand(Command):
    def executeCommand(self):
        self.receiver.bakeChickenWing()

    def __str__(self):
        return '命令模式.烤鸡翅'


class Waiter:
    def __init__(self):
        self.orders = []

    def setOrder(self, command):
        if str(command) == '命令模式.烤鸡翅':
            print('服务员：鸡翅没有了，请点别的烧烤')
        else:
            self.orders.append(command)
            print('增加订单：' + str(command) + ' 时间：' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def cancelOrder(self, command):
        self.orders.remove(command)
        print('取消订单：' + str(command) + ' 时间：' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def notify(self):
        for command in self.orders:
            command.executeCommand()


class Barbecuer:
    def bakeMutton(self):
        print('烤羊肉串！')

    def bakeChickenWing(self):
        print('烤鸡翅！')


def main():
    # 开店前的准备
    boy = Barbecuer()
    bakeMuttonCommand1 = BakeMuttonCommand(boy)
    bakeMuttonCommand12 = BakeMuttonCommand(boy)
    bakeChickenWingCommand1 = BakeChickenWingCommand(boy)
    girl = Waiter()

    # 开门营业
    girl.setOrder(bakeMuttonCommand1)
    girl.setOrder(bakeMuttonCommand12)
    girl.setOrder(bakeChickenWingCommand1)
    girl.notify()


main()

