class A:
    def show(self):
        print("A....")

class B(A):
    def show(self):
        print("B....")

b = B()
# b.__new__(A).show()
b.__class__ = A
b.show()