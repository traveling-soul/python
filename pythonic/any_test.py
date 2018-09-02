# 判断诸多条件是否至少有一个成立
math, physics, computer = 70, 40, 80
# if math < 60 or physics < 60 or computer < 60:
if any([math < 60, physics < 60, computer < 60]):
    print("not pass")
