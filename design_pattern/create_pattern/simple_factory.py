"""
用C++、Java、C#或VB.NET任意一种面向对象语言实现一个计算器控制台程序，要求输入两个数和运算符号，得到结果
设计模式：简单工厂模式，违背了开放封闭原则
"""


class Operation:
    """
    __init__()在对象初始化时自动调用，工厂模式中的方法一般为静态方法
    对象的三大特征：
    封装：隐藏了操作的细节
    继承：降低了代码的耦合度，对修改封闭，对增加开放（OCP）
    多态：增强了代码的拓展性
    """
    # def __init__(self, num1, num2):
    #     self._num1 = num1
    #     self._num2 = num2
    #     self.result = 0
    _num1 = 0
    _num2 = 0

    def set_num1(self, num1):
        self._num1 = num1

    def get_num1(self):
        return self._num1

    def set_num2(self, num2):
        self._num2 = num2

    def get_num2(self):
        return self._num2

    def get_result(self):
        return self.result


# oper = Operation(3, 4)
# print(oper.get_num1())
# oper.set_num1(5)
# print(oper.get_num1())

class AddOperation(Operation):
    def get_result(self):
        result = self.get_num1() + self.get_num2()
        return result


class MinusOperation(Operation):
    def get_result(self):
        result = self.get_num1() - self.get_num2()
        return result


class OperationFactory():
    @staticmethod
    def create_operation(operator):
        operation = None
        if operator == '+':
            operation = AddOperation()
        elif operator == "-":
            operation = MinusOperation()
        return operation


operation = OperationFactory.create_operation('+')
operation.set_num1(3)
operation.set_num2(5)
result = operation.get_result()
print(result)






