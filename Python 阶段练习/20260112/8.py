# 统计列表中正数的个数
def count_positive(lst):
    count = 0
    i = 0
    while i < len(lst):   # while i < ___？
        if lst[i] > 0:
            count += 1
        i += 1
    return count

list1 = [1,2,3,4,-1,-2,-3]
print(count_positive(list1))