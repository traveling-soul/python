from abc import abstractmethod, ABCMeta


class HandsetSoft(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass


class HandsetGame(HandsetSoft):
    def run(self):
        print('运行手机游戏')


class HandsetAddressList(HandsetSoft):
    def run(self):
        print('运行手机通讯录')


class HandsetBrand(metaclass=ABCMeta):
    soft = None

    def setHandsetSoft(self, soft):
        self.soft = soft

    def run(self):
        pass


class HandsetBrandM(HandsetBrand):
    def __init__(self):
        print('手机品牌M:')

    def run(self):
        self.soft.run()


class HandsetBrandN(HandsetBrand):
    def __init__(self):
        print('手机品牌N:')

    def run(self):
        self.soft.run()


if __name__ == '__main__':
    brand = HandsetBrandM()
    brand.setHandsetSoft(HandsetGame())
    brand.run()

    brand.setHandsetSoft(HandsetAddressList())
    brand.run()

    brand = HandsetBrandN()
    brand.setHandsetSoft(HandsetGame())
    brand.run()

    brand.setHandsetSoft(HandsetAddressList())
    brand.run()