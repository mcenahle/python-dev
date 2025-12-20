"""
小贝建了一个公众号记录自己的北漂生活，她决定每天都记录一下公众号的涨粉数量。请按照下面步骤实现代码：
定义一个名为 check_growth() 的函数，函数有一个参数 growth，即当日涨粉量；
check_growth() 函数会检查 growth 是否为空，如果不为空就把涨粉量打印出来，否则就打印出变量 tip 中保存的提示 你忘记记录今天的涨粉量了；
使用 input() 函数来输入今天的涨粉量，并传给 check_growth() 函数来检查获取到的用户输入是否为空字符串。
tip = '你忘记记录今天的涨粉量了'
"""
tip = '你忘记记录今天的涨粉量了'
def check_growth(growth):
    if growth:
        print(growth)
        return growth
    else:
        print(tip)
        return tip

growth = int(input("输入今天的涨粉量"))
check_growth(growth)