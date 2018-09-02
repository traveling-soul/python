"""
门面模式：门面、系统、客户端
将客户端与子系统解耦，减少对象的交互
门面没有对对象进行封装，对对象进行了组合
"""
class Stock1:
    def sell(self):
        print('股票1卖出')

    def buy(self):
        print('股票1买入')


class Stock2:
    def sell(self):
        print('股票2卖出')

    def buy(self):
        print('股票2买入')


class Stock3:
    def sell(self):
        print('股票3卖出')

    def buy(self):
        print('股票3买入')


class NationalDebt1:
    def sell(self):
        print('国债1卖出')

    def buy(self):
        print('国债1买入')


class Realty1:
    def sell(self):
        print('房地产1卖出')

    def buy(self):
        print('房地产1买入')


class Fund:
    def create(self):
        self.gu1 = Stock1()
        self.gu2 = Stock2()
        self.gu3 = Stock3()
        self.nd1 = NationalDebt1()
        self.rt1 = Realty1()

    def buy_fund(self):
        self.gu1.buy()
        self.gu2.buy()
        self.gu3.buy()
        self.nd1.buy()
        self.rt1.buy()

    def sell_fund(self):
        self.gu1.sell()
        self.gu2.sell()
        self.gu3.sell()
        self.nd1.sell()
        self.rt1.sell()


if __name__ == '__main__':
    jijin = Fund()
    jijin.create()
    jijin.buy_fund()
    jijin.sell_fund()
