"""
二分搜索：列表有序，找到指定元素返回元素下标，找不到则返回-1
"""
def binary_search(key, ls):
    left = 0
    right = len(ls) -1

    while left <= right:
        mid = (left + right) // 2

        if key == ls[mid]:
            print('找到了')
            return mid
        elif key < ls[mid]:
            right = mid - 1
        elif key > ls[mid]:
            left = mid + 1
    print('找不到')
    return -1

ls = [10, 4, 8, 6, 3]
# 排序
ls.sort()
print(binary_search(4, ls))


