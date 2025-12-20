time = 11
if time < 12:
    lunch = '油泼面'
else:
    lunch = '汉堡'
print('中午吃' + lunch)

# 改写为三元表达式：
time = 11
lunch = '油泼面' if time < 12 else '汉堡'
print('中午吃' + lunch)