# 计算 100*99*98*...*2*1。
i = 100
result = 1
while 1 <= i <= 100:
    result *= i
    i -= 1
print(result)