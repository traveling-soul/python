"""
开发一个可以个人搭配不同的服饰的系统
类似QQ、网络游戏或论坛都有的Avatar系统
设计模式：装饰设计模式
"""


class Person:
    """Person类"""
    def __init__(self, name):
        self.name = name

    def show(self):
        print("装扮的{}".format(self.name))


class Finery():
    def __init__(self):
       self.person = None

    def decorate(self, person):
        self.person = person

    def show(self):
        if self.person != None:
            self.person.show()


class Tshirts(Finery):
    def show(self):
        print("大T恤 ", end="")
        super(Tshirts, self).show()
        # super().show()


class BigTrouser(Finery):
    def show(self):
        print("垮裤 ", end="")
        super(BigTrouser, self).show()
        # super().show()

class Sneaker(Finery):
    def show(self):
        print("运动鞋 ", end="")
        super().show()


class LeatherShoes(Finery):
    def show(self):
        print("皮鞋 ", end="")
        super().show()


class Shirts(Finery):
    def show(self):
        print("衬衫 ", end=" ")
        super().show()


class Tie(Finery):
    def show(self):
        print("领带 ", end=" ")
        super().show()


if __name__ == "__main__":
    p = Person("小菜")
    b = BigTrouser()
    t = Tshirts()

    b.decorate(p)
    t.decorate(b)
    t.show()


