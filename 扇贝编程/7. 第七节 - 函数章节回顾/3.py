def f(x):
    y = 2 * x + 1
    if x > 2:
        # print(y)
        return y
    else:
        # print(y + 1)
        return y + 1

print(f(2))
print(f(5))

# x = 2时，y = 6（第2行，y=2*2+1=5；第7行，y+1结果为6）；x = 5时，y = 11（2*5+1）。