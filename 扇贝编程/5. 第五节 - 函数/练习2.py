"""
用函数写一个年龄计算器吧！（今年为2025年，计算2001年、1996年、1988年的年龄）

要求：
定义一个名为 calc_age 的函数；
calc_age() 函数的输入参数为出生年份，返回年龄；
调用函数三次，传入不同参数，使用 print() 函数在屏幕上打印出函数的返回值。
"""
def calc_age(year):
    age = 2025 - year
    return age
print(calc_age(2001))
print(calc_age(1996))
print(calc_age(1988))

sample_number = 5
def example_function(a):    # 定义函数，以 a 作为之后的输入数值
    b = sample_number + a  # 给出一个 b，在 sample_number + a 之后能算出 b
    return b    # 返回 b
print(example_function(2025))   # 调用函数，以 2025 作为输入数值。最终计算：2025 + sample_number。