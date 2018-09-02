def bubble_sort(ls):
    length = len(ls)
    # 比较趟数
    for j in range(length):
        # 每趟的比较次数
        for i in range(j):
            if ls[i] >= ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
    return ls


# print(bubble_sort([3, 2, 18, 12, 20]))


# 求最大值和最小值
def extremum(ls):
    max = ls[0]
    min = ls[0]

    for i in range(len(ls)):
        if ls[i] > max:
            max = ls[i]

    for j in range(len(ls)):
        if ls[j] < min:
            min = ls[j]

    return max, min


max, min = extremum([3, 2, 18, 12, 20])
print(max, min)
