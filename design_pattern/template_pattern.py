"""
小学数学老师随堂测验，在黑板上写下题目，学生先抄题目，然后再做答案，
在这个过程中，有可能将题目抄错，用什么模式可以避免这个问题？

模板方法模式：将不变的行为抽象为父类方法，将可变的行为交给子类实现，实现了代码复用
定义了一个算法的步骤，并允许子类别为一个或多个步骤提供其实践方式。
让子类别在不改变算法架构的情况下，重新定义算法中的某些步骤

使用场景：事务处理的步骤具有共性，只是具体实施，根据处理步骤中的实现的方法产生差异化。
"""

from abc import abstractmethod


class TestPaper:
    def test_question1(self):
        print("杨过得到，后来给了郭靖，炼成倚天剑、屠龙刀的玄铁可能是[] a.球磨铸铁 b.马口铁 c.高速合金钢 d.碳素纤维")

    def test_question2(self):
        print("杨过、程英、陆无双铲除了情花，造成[] a.使这种植物不再害人 b.使一种珍稀物种灭绝 c.破坏了那个生物圈的平衡 d.造成该地区沙漠化")

    def test_question3(self):
        print("蓝凤凰致使华山师徒、桃谷六仙呕吐不止，如果你是大夫，会给他们开什么药[] a.阿司匹林 b.牛黄解毒片 c.氟哌酸 d.让他们和大量的生牛奶 e.以上全不对")

    @abstractmethod
    def answer1(self):
        pass

    @abstractmethod
    def answer2(self):
        pass

    @abstractmethod
    def answer3(self):
        pass


class TestPaperA(TestPaper):
    def test_question1(self):
        super().test_question1()

    def test_question2(self):
        super().test_question2()

    def test_question3(self):
        super().test_question3()

    def answer1(self):
        return "b"

    def answer2(self):
        return "c"

    def answer3(self):
        return "c"


class TestPaperB(TestPaper):
    def test_question1(self):
        super().test_question1()

    def test_question2(self):
        super().test_question2()

    def test_question3(self):
        super().test_question3()

    def answer1(self):
        return "c"

    def answer2(self):
        return "a"

    def answer3(self):
        return "a"


if __name__ == "__main__":
    print("学生甲抄的试卷：")
    a = TestPaperA()
    a.test_question1()
    a.test_question2()
    a.test_question3()

    print("学生乙抄的试卷：")
    b = TestPaperB()
    b.test_question1()
    b.test_question2()
    b.test_question3()