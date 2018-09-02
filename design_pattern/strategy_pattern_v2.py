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


class CashContext:
    """上下文类"""
    def __init__(self, cs):
        # cs表示具体的收费实例
        self.cs = cs

    def get_result(self, money):
        # 调用收费实例的方法
        return self.cs.accept_cash(money)


if __name__ == '__main__':
    cc = None
    money = int(input('请输入应收的金额：\n'))
    type = input('请输入收费类型：\n')
    if type == '正常收费':
        cc = CashContext(CashNormal())
    elif type == '满300返100':
        cc = CashContext(CashReturn(300, 100))
    elif type == '打8折':
        cc = CashContext(CashRebate(0.8))

    cash_accept = cc.get_result(money)
    print('实收金额：{}'.format(cash_accept))

