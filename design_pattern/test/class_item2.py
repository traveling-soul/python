# class List:
#     def __init__(self):
#         self.items = []
#
#     def __getitem__(self, index):
#         return self.items[index]
#
#     def __setitem__(self, index, value):
#         self.items.insert(index, value)
#
#
# ls = List()
# ls[0] = 1
# ls[1] = 2
# for item in ls:
#     print(item)


class Student:
    def __init__(self):
        self.items = []

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, student):
        self.items.insert(index, student)


stu = Student()
stu[0] = 'mike'
stu[1] = 'jack'
for item in stu:
    print(item)
