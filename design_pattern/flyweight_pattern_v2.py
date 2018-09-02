"""
享元模式：支持大量细粒度的对象，减少实例，节约内存
"""
from abc import ABCMeta, abstractmethod


# 用户类，不共享部分
class User:
     def __init__(self, name):
         self.name = name

# 网站抽象类
class WebSite(metaclass=ABCMeta):
    @abstractmethod
    def use(self, user):
        pass


# 具体网站类，共享部分
class ConcreteWebSite(WebSite):
    def __init__(self, name):
        self.name = name

    def use(self, user):
        print("网站分类：" + self.name + " 用户：" + user.name)


# 网站工厂类
class WebSiteFactory:
    def __init__(self):
        self.flyweights = dict()

    def get_site_category(self, key):
        if not key in self.flyweights:
            self.flyweights[key] = ConcreteWebSite(key)
        return self.flyweights[key]

    def get_website_count(self):
        return len(self.flyweights)


def main():
    f = WebSiteFactory()

    fx = f.get_site_category("产品展示")
    fx.use(User("小菜"))

    fy = f.get_site_category("产品展示")
    fy.use(User("大鸟"))

    fz = f.get_site_category("产品展示")
    fz.use(User("娇娇"))

    fl = f.get_site_category("博客")
    fl.use(User("老顽童"))

    fm = f.get_site_category("博客")
    fm.use(User("桃谷六仙"))

    fn = f.get_site_category("博客")
    fn.use(User("南海鳄神"))

    print('网站分类总数为 {0}'.format(f.get_website_count()))


main()