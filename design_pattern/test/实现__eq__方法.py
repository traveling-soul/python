class A:
    pass


a = A()
b = a
print(a == b)
print(hasattr(a, '__eq__'))
a.__eq__