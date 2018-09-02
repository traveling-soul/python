def fibs():
    first = 1
    second = 1
    yield first
    yield second
    while True:
        yield first + second
        first, second = second, first + second


def show_fibs(n):
    assert isinstance(n, int) and n >= 0
    it = fibs()  # it是生成器对象
    for i in range(n):
        print(next(it))


show_fibs(10)
