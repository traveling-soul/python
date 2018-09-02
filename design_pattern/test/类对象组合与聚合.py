# #! /usr/bin/env python
# # coding:utf-8
#
# '''
# 类对象聚合关系
# '''
#
#
# class Cpu(object):
#
#     def __init__(self):
#         self.type = '286'
#
#
# class Computer(object):
#
#     def __init__(self, cpu):
#         self.cpu = cpu  # 有一个CPu类的实例对象
#
#     def __del__(self):
#         print ("没有权力和Cpu by by!")
#
# old_cpu = Cpu()
# old_computer = Computer(old_cpu)
# del old_computer

#! /usr/bin/env python
# coding:utf-8

'''
类对象组合关系
'''

class Cpu(object):

    def __init__(self):
        self.type = '286'


class Computer(object):

    def __init__(self):
        self.cpu = Cpu()  # 包含CPu类的实例对象

    def __del__(self):
        print ("Cpu by by!")

old_computer = Computer()
del old_computer