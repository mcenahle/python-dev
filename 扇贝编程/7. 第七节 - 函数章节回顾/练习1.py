"""
爱因斯坦在 1905 年提出了质能方程，即 E = mc²（E 表示能量、m 表示质量、c 表示光速）。接下来我们使用质能方程编写一个计算物体所拥有能量的函数。
要求：
将名为 calc_energy 的函数补全；
函数参数 m 表示物体质量；
打印出质量为 2 个单位和 3 个单位的物体所拥有能量。
提示：光速近似为 300000000 m/s。
示例：def calc_energy(???):
  c = 300000000
  E = ??? * c * c
  ???
print(calc_energy(???))
print(calc_energy(???))
"""
def calc_energy(quality):
    c = 300000000
    e = quality * c * c
    return e
print(calc_energy(2))
print(calc_energy(3))