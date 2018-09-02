# 判断是否为多个取值之一
level = 'C'
# if level == 'A' or level == 'B' or level == 'C':
if level in ('A', 'B', 'C'):
    status = 'pass'
print(status)
