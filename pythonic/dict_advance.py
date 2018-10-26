#coding=utf8
"""
data = [("p", 1), ("p", 2), ("p", 3),
        ("h", 1), ("h", 2), ("h", 3)]

要转换成

result = {'p': [1, 2, 3], 'h': [1, 2, 3]}
"""

data = [("p", 1), ("p", 2), ("p", 3),
        ("h", 1), ("h", 2), ("h", 3)]
result = {}
# for (key, value) in data:
#     if key in result:
#         result[key].append(value)
#     else:
#         result[key] = [value]

# d = {"x": 3}
# y = d.get("y", 4)
# print(y)
# print(d)

# y = d.setdefault("y", 4)
# print(y)
# print(d)

# for (key, value) in data:
#     result.setdefault(key, []).append(value)


from collections import defaultdict
result = defaultdict(list)
for (key, value) in data:
    result[key].append(value)
print(result)
