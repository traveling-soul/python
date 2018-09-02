"""
假设有一个网上咖啡选购平台，客户可以在该平台上下订单订购咖啡，平台会根据用户位置进行线下配送。

享元模式：支持大量细粒度的对象，减少实例，节约内存
运用共享技术有效支持大量细粒度对象。
在享元对象内部并且不会随环境改变而改变的共享部分，可以称为是享元对象的内部对象，
而随环境改变而改变的、不可以共享的状态就是外部状态了。
享元模式可以避免大量非常相似类的开销。
在程序设计中，有时需要生成大量细粒度的类实例来表示数据。
如果能发现这些实例除了几个参数外基本相同的，有时就能够大幅度减少需要实例化的类的数量，
如果能把这些参数移到类实例的外面，在方法调用时将他们传递进来，就可以通过共享大幅度减少单个实例的数目。

适用场景：
1、系统中存在大量的相似对象时，可以选择享元模式；
2、需要缓冲池的场景中，如进程池、线程池等技术。
"""


# 顾客类：外部状态，非共享代码
class Customer:
    name = ""
    coffee_factory = ""

    def __init__(self, name, coffee_factory):
        self.name = name
        self.coffee_factory = coffee_factory

    def order(self, coffee_name):
        print("%s order a cup of coffee:%s" % (self.name, coffee_name))
        return self.coffee_factory.get_coffee_name(coffee_name)


# 咖啡类：内部状态，共享代码
class Coffee:
    name = ""
    price = 0
    def __init__(self, name):
        self.name = name
        self.price = len(name)

    def show(self):
        print("Coffee Name:%s Price:%s" % (self.name, self.price))


# 咖啡工厂，生成咖啡实例
class CoffeeFactory:
    coffee_dict = dict()

    def get_coffee_name(self, name):
        if not self.coffee_dict.get(name, False):
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]

    def get_coffee_count(self):
        return len(self.coffee_dict)


def main():
    coffee_factory = CoffeeFactory()

    customer1 = Customer("client1", coffee_factory)
    customer1.order("卡布奇诺")

    customer2 = Customer("client2", coffee_factory)
    customer2.order("卡布奇诺")

    customer3 = Customer("client3", coffee_factory)
    customer3.order("摩卡")

    customer4 = Customer("client4", coffee_factory)
    customer4.order("拿铁")

    print("CoffeeFactory中coffee的实例对象数：", coffee_factory.get_coffee_count())


main()