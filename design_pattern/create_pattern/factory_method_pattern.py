"""
Django 的 forms 模块使用工厂方法模式来创建表单字段。
WTForm 也使用到了工厂方法模式。
sqlalchemy 中不同数据库连接部分也用到了工厂方法模式。
"""
class LeiFeng:
    def sweep(self):
       print('扫地')

    def wash(self):
        print('洗衣')

    def buy_rice(self):
        print('买米')


class LeiFengFactory:
    def create_leifeng(self):
        pass


class Undergraduate(LeiFeng):
    pass


class Volunteer(LeiFeng):
    pass


class UnderGraduateFactory(LeiFengFactory):
    def create_leifeng(self):
        return Undergraduate()


class VolunteerFactory(LeiFengFactory):
    def create_leifeng(self):
        return Volunteer()


if __name__ == '__main__':
    stu_factory = UnderGraduateFactory()
    stu = stu_factory.create_leifeng()
    stu.sweep()

    stu2 = stu_factory.create_leifeng()
    stu.wash()

    stu3 = stu_factory.create_leifeng()
    stu3.buy_rice()