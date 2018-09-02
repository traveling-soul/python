import types

class A:
    pass

class B(A):
    pass


class C(B):
    pass

# print(B.__mro__)
# print(B.__bases__)
# print(C.__mro__)
# print(C.__bases__)

import inspect
print(inspect.getmro(B))
