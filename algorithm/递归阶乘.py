# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)


# print(factorial(1000))


# 优化，尾递归--当递归调用是函数体中最后执行的语句并且它的返回值不属于表达式一部分时， 这个递归就是尾递归。
def factorial2(n, result):
    if n == 1:
        return result
    return factorial2(n - 1, n * result)


print(factorial2(1000, 1))
