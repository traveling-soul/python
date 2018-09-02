# import bisect
# import sys
#
#
# def grade(score, breakpoint=[60, 70, 80, 90], grades = 'FDCBA'):
#     i = bisect.bisect(breakpoint, score)
#     return grades[i]
#
# if __name__ == '__main__':
#     level = grade(42)
#     print(level)

# from collections import UserDict
#
# li = [
#     {'id': '1.1', 'content': "14"},
#     {'id': '1.2', 'content': "15"},
#     {'id': '1.3', 'content': "16"},
#     {'id': '1.4', 'content': "17"},
#     {'id': '1.5', 'content': "18"},
# ]
#
# class x(UserDict):
#
#     def __init__(self):
#         super().__init__()
#         for dic in li:
#             # print(dic)
#             self.data.update({dic['id']:dic['content']})
#
# abc = x()
# print(abc['1.1'])

ls = [1, 2, 2, 5, 5, 6, 2]
ls2 = list(dict.fromkeys(ls))
print(ls2)

