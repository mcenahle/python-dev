"""
小新一家最近家里装修，临时搬到了“鸡飞狗跳院”，要住一年，房租每月 3500 元。小新用学过的函数知识写了一个房租计算器来计算一年的房租，但总是运行报错。你能运用刚刚学过的变量作用域的知识，能帮小新改正程序中的错误吗？
total_rent = 0
def calc_rent(n, rent):
    total_rent = n * rent
calc_rent(12, 3500)
print(total_rent)
"""

total_rent = 0
def calc_rent(n, rent):
    global total_rent
    total_rent = n * rent
calc_rent(12, 3500)
print(total_rent)