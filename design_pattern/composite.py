"""
OA系统（办公自动化系统）：总公司使用，子公司或办事处也要使用
目的：将对象组合成树形结构，以表示”部分-整体”的层次结构，使得用户对单个对象和组合对象的使用具有一致性
"""
from abc import ABCMeta, abstractmethod


class Company(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def add(self, company):
        pass

    @abstractmethod
    def remove(self, company):
        pass

    @abstractmethod
    def display(self, depth):
        pass

    @abstractmethod
    def line_of_duty(self):
        pass


class ConcreteCompany(Company):
    def __init__(self, name):
        self.name = name
        self.companies = []

    def add(self, company):
        self.companies.append(company)

    def remove(self, company):
        self.companies.remove(company)

    def display(self, depth):
        print('-'*depth + self.name)
        for c in self.companies:
            c.display(depth+2)

    def line_of_duty(self):
        for c in self.companies:
            c.line_of_duty()


class HRDepartment(Company):
    def add(self, company):
        pass

    def remove(self, company):
        pass

    def display(self, depth):
        print('-'*depth+self.name)

    def line_of_duty(self):
        print('{} 员工招聘培训管理'.format(self.name))


class FinanceDepartment(Company):
    def add(self, company):
        pass

    def remove(self, company):
        pass

    def display(self, depth):
        print('-' * depth + self.name)

    def line_of_duty(self):
        print('{} 公司财务收支管理'.format(self.name))


if __name__ == '__main__':
    root = ConcreteCompany('北京总公司')
    root.add(HRDepartment('总公司人力资源部'))
    root.add(FinanceDepartment('总公司财务部'))

    comp = ConcreteCompany('上海华东分公司')
    comp.add(HRDepartment('华东分公司人力资源部'))
    comp.add(FinanceDepartment('华东分公司财务部'))
    root.add(comp)

    comp1 = ConcreteCompany('南京办事处')
    comp1.add(HRDepartment('南京办事处人力资源部'))
    comp1.add(FinanceDepartment('南京办事处财务部'))
    comp.add(comp1)

    comp2 = ConcreteCompany('杭州办事处')
    comp2.add(HRDepartment('杭州办事处人力资源部'))
    comp2.add(FinanceDepartment('杭州办事处财务部'))
    comp.add(comp2)

    print('\n结构图：')
    root.display(1)

    print('\n职责：')
    root.line_of_duty()