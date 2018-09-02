from abc import abstractmethod, ABCMeta


class Command(metaclass=ABCMeta):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def executeCommand(self):
        pass


class BakeMuttonCommand(Command):
    def executeCommand(self):
        self.receiver.bakeMutton()


class BakeChickenWingCommand(Command):
    def executeCommand(self):
        self.receiver.bakeChickenWing()


class Waiter:
    def setOrder(self, command):
        self.command = command

    def notify(self):
        self.command.executeCommand()


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
    girl.notify()
    girl.setOrder(bakeMuttonCommand12)
    girl.notify()
    girl.setOrder(bakeChickenWingCommand1)
    girl.notify()


main()

