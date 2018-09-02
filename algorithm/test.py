# def log(func):
#     def inner():
#         print('call ' + func.__name__ + '()')
#         func()
#     return inner
#
#
# @log
# def now():
#     print('2013-12-25')
#
#
# now()


# myset2=set("abcdefg")
# myset3=set("abcdxyz")
# newset = myset2.union(myset3)
# diff = myset2.difference(myset3)
# print(newset)
# print(diff)


# def filter_impl(func, args):
#     res = []
#
#     for arg in args:
#         if func(arg):
#             res.append(arg)
#     return res
#
#
# print(filter_impl((lambda x: x < 4), range(1, 10)))


# def map_impl(func, args):
#     res = []
#     for arg in args:
#         res.append(func(arg))
#     return res
#
# print(map_impl((lambda x: x*x), range(1, 11)))


# def reduce_impl(func, args):
#     arg1 = args[0]
#     for arg2 in args[1:]:
#         arg1 = func(arg1, arg2)
#     return arg1
#
#
# print(reduce_impl((lambda x, y: x + y), range(1, 11)))

# print(list(map((lambda x: x.capitalize()), ['adam', 'LISA', 'barT'])))

# from functools import partial
#
# int2 = partial(int, base=2)
# print(int2('10010'))
# print(int2('10010', base=10))

import re

# with open('1.txt', 'r') as f:
#     dictResult = {}
#
#     # 每次读取一行的文件
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         listMatch = re.findall('\b(\w+)\b', line.lower())  # 转为小写字母
#         print(listMatch)
#         # 计数
#         for eachLetter in listMatch:
#             eachLetterCount = len(re.findall(eachLetter, line.lower()))
#             dictResult[eachLetter] = dictResult.get(eachLetter, 0) + eachLetterCount
#
#     # 从大到小排序
#     result = sorted(dictResult.items(), key=lambda d: d[1], reverse=True)[:3]
#     for each in result:
#         print(each)
# ('a', 275)
# ('to', 119)
# ('the', 77)


#
# print(c) # 'to': 23, 'the': 16, 'a': 14
# print(len(c))

