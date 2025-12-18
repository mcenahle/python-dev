def math(x):
    y = x + 1
    print(y)

print(math(3))

# math(3) 的结果就是 3+1=4。
# 由于是 print(y)，而不是 return y，所以最后再返回一个 None。
# 如果是 return y，则会是这样，返回一个 4:
def math(x):
    y = x + 1
    return y

print(math(3))