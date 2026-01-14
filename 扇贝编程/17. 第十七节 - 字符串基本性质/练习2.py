"""小贝在一家水果店兼职，今天进货的水果都存在列表 fruits 中。
不过，老板觉得，列表打印出来的效果太丑了，老板想要小贝统一按照 Apple--Pineapple--Banana--Apple 这样的形式将进货清单打印出来，要求：
首字母大写；
不同水果之间的连接符为 --。
整理完成后，小贝还需要统计一下今天进了多少份苹果，并将统计的结果按照 今天进了n斤苹果 的格式打印出来，n是苹果进货的斤数。"""

fruits = ['Apple', 'pineapple', 'banana', 'apple', 'peach', 'strawberry', 'apple', 'pineapple', 'banana', 'orange', 'peach', 'apple', 'watermelon']
# 将进货清单按老板给的格式输出
fruits_str = ('--'.join(fruits)).title()
print(fruits_str)

# 统计今天进了多少份苹果
n = fruits_str.count('Apple')
print('今天进了' + str(n) + '斤苹果')