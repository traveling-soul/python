class DoubleFloat(float):
    def __new__(cls,arg = .6):
        print(cls)
        return float.__new__(cls, arg * 2)


a = DoubleFloat()
print(a)

b = DoubleFloat(1.9)
print(b)