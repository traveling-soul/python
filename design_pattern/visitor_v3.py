"""
男人与女人的不同
"""
from abc import ABCMeta, abstractmethod

# 状态抽象类
class Action(metaclass=ABCMeta):
    @abstractmethod
    def get_man_conclusion(self, man):
        pass

    @abstractmethod
    def get_woman_conclusion(self, woman):
        pass

# 人类
class Person(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, action):
        pass


# 男人类
class Man(Person):
    def accept(self, action):
       action.get_man_conclusion(self)

    def __str__(self):
        return "男人"

# 女人类
class Woman(Person):
    def accept(self, action):
        action.get_woman_conclusion(self)

    def __str__(self):
        return "女人"


# 成功
class Success(Action):
    def get_man_conclusion(self, man):
        print("{0}{1}时，背后多半有一个伟大的女人。".format(str(man), str(self)))

    def get_woman_conclusion(self, woman):
        print("{0}{1}时，背后大多有一个不成功的男人。".format(str(woman), str(self)))

    def __str__(self):
        return "成功"


# 失败
class Failing(Action):
    def get_man_conclusion(self, man):
        print("{0}{1}时，闷头喝酒，谁也不用劝。".format(str(man), str(self)))

    def get_woman_conclusion(self, woman):
        print("{0}{1}时，眼泪汪汪，谁也劝不了。".format(str(woman), str(self)))

    def __str__(self):
        return "失败"


# 恋爱
class Amativeness(Action):
    def get_man_conclusion(self, man):
        print("{0}{1}时，凡是不懂也要装懂。".format(str(man), str(self)))

    def get_woman_conclusion(self, woman):
        print("{0}{1}时，遇事懂也装作不懂。".format(str(woman), str(self)))

    def __str__(self):
        return "恋爱"


# 结婚
class Marriage(Action):
    def get_man_conclusion(self, man):
        print("{0}{1}时，感慨道：恋爱游戏终结时，‘有妻徒刑’遥无期。".format(str(man), str(self)))

    def get_woman_conclusion(self, woman):
        print("{0}{1}时，欣慰曰：爱情长跑路漫漫，婚姻保险报平安。".format(str(woman), str(self)))

    def __str__(self):
        return "结婚"


# 对象结构
class ObjectStructure:
    def __init__(self):
        self.persons = []

    # 增加
    def attach(self, person):
        self.persons.append(person)

    # 移除
    def detatch(self, person):
        self.persons.remove(person)

    # 查看显示
    def display(self, action):
        for person in self.persons:
            person.accept(action)


def main():
    o = ObjectStructure()
    o.attach(Man())
    o.attach(Woman())

    # 成功时的反应
    success = Success()
    o.display(success)

    # 失败时的反应
    fail = Failing()
    o.display(fail)

    # 恋爱时的反应
    amative = Amativeness()
    o.display(amative)

    # 结婚时的状态
    marriage = Marriage()
    o.display(marriage)


main()