"""
男人与女人的不同
"""
from abc import ABCMeta, abstractmethod


# 人类
class Person(metaclass=ABCMeta):
    def __init__(self):
        self.action = ""

    @abstractmethod
    def get_conslusion(self):
        pass


# 男人类
class Man(Person):
    def get_conslusion(self):
        if self.action == "成功":
            print("{0}{1}时，背后多半有一个伟大的女人。".format(str(self), self.action))
        elif self.action == "失败":
            print("{0}{1}时，闷头喝酒，谁也不用劝。".format(str(self), self.action))
        elif self.action == "恋爱":
            print("{0}{1}时，凡是不懂也要装懂。".format(str(self), self.action))

    def __str__(self):
        return "男人"

# 女人类
class WoMan(Person):
    def get_conslusion(self):
        if self.action == "成功":
            print("{0}{1}时，背后大多有一个不成功的男人。".format(str(self), self.action))
        elif self.action == "失败":
            print("{0}{1}时，眼泪汪汪，谁也劝不了。".format(str(self), self.action))
        elif self.action == "恋爱":
            print("{0}{1}时，遇事懂也装作不懂。".format(str(self), self.action))

    def __str__(self):
        return "女人"


def main():
    persons = []

    man1 = Man()
    man1.action = "成功"
    persons.append(man1)
    woman1 = WoMan()
    woman1.action = "成功"
    persons.append(woman1)

    man2 = Man()
    man2.action = "失败"
    persons.append(man2)
    woman2 = WoMan()
    woman2.action = "失败"
    persons.append(woman2)

    man3 = Man()
    man3.action = "恋爱"
    persons.append(man3)
    woman3 = WoMan()
    woman3.action = "恋爱"
    persons.append(woman3)

    for person in persons:
        person.get_conslusion()

main()