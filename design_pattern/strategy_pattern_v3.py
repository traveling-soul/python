"""
做一个商场收银软件，营业员根据客户所购买商品的单价和数量，向客户收费
收费模式：
        正常收费
        满300返100
        打8 折
设计模式：策咯模式
策咯模式
"""
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
            result = money - math.floor(money / self.money_condition) * self.money_return
        return result


class CashContext:
    """上下文类"""
    def __init__(self, type):
        # cs表示具体的收费实例
        if type == '正常收费':
            self.cs = CashNormal()
        elif type == '满300返100':
            self.cs = CashReturn(300, 100)
        elif type == '打8折':
            self.cs = CashRebate(0.8)

    def get_result(self, money):
        # 调用收费实例的方法
        return self.cs.accept_cash(money)


if __name__ == '__main__':
    money = int(input('请输入应收的金额：\n'))
    type = input('请输入收费类型：\n')
    cc = CashContext(type)
    cash_accept = cc.get_result(money)
    print('实收金额：{}'.format(cash_accept))

