ls = [1, 3, 4, 5, 6, 10]
res = filter((lambda x: x % 2 == 1), ls)
print(res)
# print(list(res))
# print(type(res))

# it = iter(res)
# while True:
#     try:
#         item = next(it)
#         print(item)
#     except StopIteration:
#         break
for i in res:
    print(i)


# def is_odd(item):
#     return item % 2 == 1


# res = filter(is_odd, ls)
# print(res)
# print(list(res))



