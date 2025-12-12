"""
小贝将上一个练习中计算年龄的函数 calc_age() 改进了一下，想要每次计算并返回年龄的同时，让函数自己在屏幕上打印通知“计算完成”。
不过他发现，在实际调用函数时，可以计算出年龄，但屏幕上没有计算完成的通知。
你能帮他改一下，让代码既可以打印返回的年龄，也可以让函数自己打印通知吗？

原文：
def calc_age(birth_year):
  age = 2024 - birth_year
  return age
  print('计算完成')

print(calc_age(2003))
"""

def calc_age(birth_year):
    age = 2024 - birth_year
    print('计算完成')
    return age
print(calc_age(2003))