from abc import abstractmethod, ABCMeta


# 申请类
class Request:
    def __init__(self):
        # 申请类型
        self.requestType = None
        # 申请内容
        self.requestContent = None
        # 数量
        self.number = None


# 管理者抽象类
class Manager(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    # 设置管理者的上级
    def setSuperior(self, superior):
        self.superior = superior

    # 申请请求
    @abstractmethod
    def requestApplication(self, request):
        pass


# 经理
class CommonManager(Manager):
    def requestApplication(self, request):
        if request.requestType == '请假' and request.number <= 2:
            print('{0}:{1} 数量{2} 被批准'.format(self.name, request.requestType, request.number))
        else:
            if self.superior:
                self.superior.requestApplication(request)


# 总监
class Majordomo(Manager):
    def requestApplication(self, request):
        if request.requestType == '请假' and request.number <= 5:
            print('{0}:{1} 数量{2} 被批准'.format(self.name, request.requestType, request.number))
        else:
            if self.superior:
                self.superior.requestApplication(request)


# 总经理
class GeneralManager(Manager):
    def requestApplication(self, request):
        if request.requestType == '请假':
            print('{0}:{1} 数量{2} 被批准'.format(self.name, request.requestType, request.number))
        elif request.requestType == '加薪' and request.number <= 500:
            print('{0}:{1} 数量{2} 被批准'.format(self.name, request.requestType, request.number))
        elif request.requestType == '加薪' and request.number > 500:
            print('{0}:{1} 数量{2} 再说吧'.format(self.name, request.requestType, request.number))


# 客户端
def main():
    jinli = CommonManager('金利')
    zongjian = Majordomo('宗剑')
    zhongjingli = GeneralManager('钟精励')
    jinli.setSuperior(zongjian)
    zongjian.setSuperior(zhongjingli)

    request = Request()
    request.requestType = '请假'
    request.requestContent = '小菜请假'
    request.number = 1
    jinli.requestApplication(request)

    request2 = Request()
    request2.requestType = '请假'
    request2.requestContent = '小菜请假'
    request2.number = 4
    jinli.requestApplication(request2)

    request3 = Request()
    request3.requestType = '加薪'
    request3.requestContent = '小菜请求加薪'
    request3.number = 500
    jinli.requestApplication(request3)

    request4 = Request()
    request4.requestType = '加薪'
    request4.requestContent = '小菜请求加薪'
    request4.number = 1000
    jinli.requestApplication(request4)


main()