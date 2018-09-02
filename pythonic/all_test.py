# 判断诸多条件是否全部成立
math, physics, computer = 70, 70, 80
# if math >= 60 and physics >= 60 and computer >= 60:
if all([math >= 60, physics >= 60, computer >= 60]):
    print('pass!')
