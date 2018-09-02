def eat_decorator(func):
    def wrapper():
        func()
        print("吃的是黄河鲤鱼")
    return wrapper


@eat_decorator
def eat():
    print("吃饭")



if __name__ == "__main__":
    eat()