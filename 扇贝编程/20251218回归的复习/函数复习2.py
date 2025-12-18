"""
用函数写一个年龄计算器吧！（今年为2025年，计算2001年、1996年、1988年的年龄）

要求：
定义一个名为 calc_age 的函数；
calc_age() 函数的输入参数为出生年份，返回年龄；
调用函数三次，传入不同参数，使用 print() 函数在屏幕上打印出函数的返回值。
要每次计算并返回年龄的同时，让函数自己在屏幕上打印通知“计算完成”。
"""

def calc_age(born_year):
    age = 2025 - born_year
    print("打印完成：")
    return age
print(calc_age(2001))
print(calc_age(1996))
print(calc_age(1988))