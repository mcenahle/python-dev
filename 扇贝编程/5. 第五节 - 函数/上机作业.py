"""
我们都知道：
三角形内角和为 180°
四边形内角和为 360°
五边形内角和为 540°
……
以此类推，n 边形的内角和的计算公式是 (n - 2) * 180。
接下来请你编写一个计算多边形内角和的函数。

要求：
定义一个名为 calc_degree 的函数
calc_degree 函数的输入为多边形的边数，输出为该多边形内角和（只需要数字即可，不需要 ° 这个符号）
在屏幕上输出 calc_degree 函数的返回值
"""
def calc_degree(n):
    degree = (n - 2) * 180
    return degree
print(calc_degree(3))
print(calc_degree(4))
print(calc_degree(5))