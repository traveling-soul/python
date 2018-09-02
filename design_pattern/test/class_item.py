# class testsetandget:
#     kk = {}
#
#     def __getitem__(self, key):
#         return self.kk[key]
#
#     def __setitem__(self, key, value):
#         self.kk[key] = value
#
# a = testsetandget()
# a['first'] = 1
# print(a['first'])
#
# a.__setitem__('second', 2)
# print(a.__getitem__('second'))


class testsetandget2:
    kk = []

    def __getitem__(self, index):
        return self.kk[index]

    def __setitem__(self, index, value):
        self.kk.insert(index, value)
ls = testsetandget2()
ls[0] = 2
ls[1] = 3
for item in ls:
    print(item)