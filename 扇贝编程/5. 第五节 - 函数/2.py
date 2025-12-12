"""
你在编程咖啡店干得不错，已经晋升为店长啦 🎉
已知的信息如下：

咖啡店目前只卖拿铁，每杯售价 24 元，成本为 8 元；
咖啡店每天的水电、人工成本为 500。
接下来请你写一个利润计算器来计算一下咖啡店每天的利润，要求：

定义一个名为 calc_profit 的函数；
该函数有一个参数，为当天卖出的拿铁数量；
函数的返回值为咖啡店当天的净利润（不需要单位）；
通过 input() 函数获取当天卖出的拿铁数量；
调用函数并打印出咖啡店当天的净利润。
"""

def calc_profit(drinks):
    earn_money = (24 - 8) * drinks - 500
    return earn_money
num = int(input("请输入当天卖出的拿铁数量："))
profit = calc_profit(num)
print(profit)
