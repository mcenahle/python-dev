# 返回列表中所有元素的和
def list_sum(lst):
    s = 0
    i = 0
    while i < len(lst):
        s += lst[i]  # s += ____
        i += 1
    return s
