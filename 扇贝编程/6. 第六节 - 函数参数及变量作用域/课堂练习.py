"""
小新要和妈妈美伢一起去超市买东西，妈妈问小新有没有想吃的零食，此时小新的脑海里就浮现出了“小熊饼干”“果汁”“牛奶”“薯片”的样子，止不住流下了口水。你能写一个多参数的函数，帮助小新将他想吃的东西都打印出来给妈妈看吗？

要求：
按顺序打印出小熊饼干、果汁、牛奶和薯片；
调用 print_foods() 函数两次，第一次使用位置参数，第二次使用关键字参数。
提示：使用关键字参数时，一定要保证参数与值对应哦。

原文：
def print_foods(food1, food2, food3, food4):
    print(food1)
    print(food2)
    print(food3)
    print(food4)

# 在下一行调用函数，使用位置参数传入

# 在下一行调用函数，补全关键字参数，注意参数与值的对应
print_foods(food4='薯片', food3=, food1=, food2=)
"""
def print_foods(food1, food2, food3, food4):
    print(food1)
    print(food2)
    print(food3)
    print(food4)

# 在下一行调用函数，使用位置参数传入
print_foods('小熊饼干', '果汁','牛奶','薯片')
print_foods(food4 = '薯片', food3 = '牛奶', food1 = '小熊饼干', food2 = '果汁')