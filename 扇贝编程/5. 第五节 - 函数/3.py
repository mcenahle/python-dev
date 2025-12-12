"""
你已经作为咖啡店店长干了一段时间了，领导想对你管理的店进行考核，考核要求很简单：每天的净利润大于 2000 为合格，否则不合格。

上一题你已经完成了计算净利润的 calc_profit() 函数，接下来请你再写一个绩效计算器来计算一下咖啡店每天是否合格，要求：

再定义一个名为 calc_perf 的函数；
该函数有一个参数，为当天的净利润（calc_profit() 函数的返回值）；
该函数功能为：当净利润大于 2000 时打印 合格，否则打印 不合格；
使用 input() 函数获取当天卖出的拿铁数量；
调用函数并打印出咖啡店当天是否合格。

原文：
def calc_profit(n):
  price =  24
  cost = 8
  profit = (price - cost) * n - 500
  return profit

n = int(input('请输入今天咖啡店的销量'))
print(calc_profit(n))
"""

# 定义一个函数，用于计算净利润
def calc_profit(n):
    price = 24       # 每杯拿铁售价
    cost = 8         # 每杯拿铁成本
    profit = (price - cost) * n - 500  # 计算净利润：总收入减去总成本和每日固定支出
    return profit    # 返回净利润

# 定义一个函数，用于判断绩效是否合格
def calc_perf(profit):
    if profit > 2000:    # 如果净利润大于2000
        print("合格")    # 输出“合格”
    else:
        print("不合格")  # 否则输出“不合格”

# 获取用户输入的当天销量
n = int(input('请输入今天咖啡店的销量：'))

# 调用函数计算净利润，并保存结果
today_profit = calc_profit(n)

# 打印净利润
print(today_profit)

# 调用函数判断绩效是否合格
calc_perf(today_profit)
