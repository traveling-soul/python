# import copy
# inner_ls = [0 for i in range(10)]
# ls = [copy.deepcopy(inner_ls) for i in range(10)]
# print(ls)
# ls[0][0] = 1
# print(ls)

data = [
    {"name": "linux", "value": 12, "accuracy_rate": 44},
    {"name": "windows", "value": 21, "accuracy_rate": 76},
    {"name": "Android", "value": 8, "accuracy_rate": 90},
    {"name": "OS X", "value": 32, "accuracy_rate": 90},
]

data.sort(key=lambda x:(x["accuracy_rate"],-x["value"]))
print(data)
