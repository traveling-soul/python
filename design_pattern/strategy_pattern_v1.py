import math


class CashSuper:
    """现金收费抽象类"""
    def accept_cash(self, money):
        pass


class CashNormal(CashSuper):
    """正常收费子类"""
    def accept_cash(self, money):
        return money


class CashRebate(CashSuper):
    """打折收费子类"""
    def __init__(self, money_rebate):
        self.money_rebate = money_rebate

    def accept_cash(self, money):
        return money * self.money_rebate


class CashReturn(CashSuper):
    """返利收费子类"""
    def __init__(self, money_condition, money_return):
        self.money_condition = money_condition
        self.money_return = money_return

    def accept_cash(self, money):
        result = 0
        if money >= self.money_condition:
            result = money - math.floor(money / self.money_conditon) * self.money_return
        return result


class CashFactory:
    """现金收费工厂类"""
    @staticmethod
    def create_cash_accept(type):
        cs = None
        if type == '正常收费':
            cs = CashNormal()
        elif type == '满300返100':
            cs = CashReturn(300, 100)
        elif type == '打8折':
            cs = CashRebate(0.8)
        return cs


if __name__ == '__main__':
    cs = CashFactory.create_cash_accept('正常收费')
    cash_accept = cs.accept_cash(300)
    print(cash_accept)
    cs2 = CashFactory.create_cash_accept('打8折')
    cash_accept2 = cs2.accept_cash(300)
    print(cash_accept2 )
