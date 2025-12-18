"""
代码改错：
def power(n = 2, x)
 y = x ** n
  return y

print(power(2))
print(power(2, 3))
"""

def power(x, n = 2):
    y = x ** n
    return y
print(power(2))
print(power(2, 3))