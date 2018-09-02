from abc import ABCMeta, abstractmethod


# 网站抽象类
class WebSite(metaclass=ABCMeta):
    @abstractmethod
    def use(self):
        pass


# 具体网站类
class ConcreteWebSite(WebSite):
    def __init__(self, name):
        self.name = name

    def use(self):
        print("网站分类：", self.name)


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
    fx.use()

    fy = f.get_site_category("产品展示")
    fy.use()

    fz = f.get_site_category("产品展示")
    fz.use()

    fl = f.get_site_category("博客")
    fl.use()

    fm = f.get_site_category("博客")
    fm.use()

    fn = f.get_site_category("博客")
    fn.use()

    print('网站分类总数为 {0}'.format(f.get_website_count()))


main()