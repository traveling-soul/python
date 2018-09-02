"""
适配器模式（Adapter）模式主要应用于希望复用一些现存的类，
但是接口又与复用环境要求不一致的情况。
通常在软件开发后期或维护期考虑使用适配器模式，
如果公司设计以一系统时考虑使用第三方开发组件，
而这个组件的接口与我们自己的系统接口是不相同的，
而我们也完全没有必要为了迎合它而改动自己的接口，
此时可以考虑适配器模式。

Target：客户端期待的接口，具体或抽象都可以
Adaptee：需要适配的类
Adpater：通过在内部包装一个Adaptee对象，把源接口转换成目标接口
"""

class Target(object):
    def request(self):
        print('普通请求')


class Adaptee(object):
    def special_request(self):
        print('特殊请求')


class Adapter(Target):
    def __init__(self):
        self.__adaptee = Adaptee()

    def request(self):
        self.__adaptee.special_request()


if __name__ == '__main__':
    target = Adapter()
    target.request()
