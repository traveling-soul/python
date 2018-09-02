from abc import ABCMeta, abstractmethod

class Player(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defense(self):
        pass


class Forwards(Player):
    def attack(self):
        print('前锋 {0} 进攻'.format(self.name))

    def defense(self):
        print('前锋 {0} 防守'.format(self.name))


class Center(Player):
    def attack(self):
        print('中锋 {0} 进攻'.format(self.name))

    def defense(self):
        print('中锋 {0} 防守'.format(self.name))


class Guards(Player):
    def attack(self):
        print('后卫 {0} 进攻'.format(self.name))

    def defense(self):
        print('后卫 {0} 防守'.format(self.name))


class ForeignCenter:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print('外籍中锋 {0} 进攻'.format(self.name))

    def defense(self):
        print('外籍中锋 {0} 防守'.format(self.name))


class Translator(Player):
    def __init__(self, name):
        self._foreign_center = ForeignCenter(name)

    def attack(self):
        self._foreign_center.attack()

    def defense(self):
        self._foreign_center.defense()


if __name__ == "__main__":
    b = Forwards('巴蒂尔')
    b.attack()
    m = Guards('麦克格雷迪')
    m.attack()

    ym = Translator('姚明')
    ym.attack()
    ym.defense()
