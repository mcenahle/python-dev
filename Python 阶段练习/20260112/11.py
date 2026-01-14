# 判断一个数是否在列表中
def in_list(x, lst):
    i = 0
    while i < len(lst):
        if lst[i] == x:  # if lst[i] == ____:
            return True
        i += 1
    return False
