letters = [
  '7', 'u', 'b', 'u', 'r', 'l', 'n', ' ', '5', 'o',
  'j', 'c', '3', '7', '1', 'x', 'd', 'x', 'm', '8',
  'a', 'v', 'f', 'd', 'z', 'z', 'd', 'l', 'v', 'o',
  'q', 'j', 'u', '2', 'o', 'l', 'v', '6', 'i', 'o',
  'i', '5', '9', 'b', 'c', 'i', 's', 'a', 'i', '2',
  '!', '8', 's', 't', '9', 'r', 'x', 'w', 'j', '1',
  '5', '5', '3', 'm', '9', '6', 'r', 'w', '9', 'd',
  'd', 'r', 'y', '3', 'p', 'h', 'f', '9', '1', 'b',
  'w', 'u', 'c', 'e', 'r', '3', 'i', 'i', 'x', '7',
  'x', '2', 'n', 'p', 'a', '4', 'b', 'f', 'w', ' '
]
# 按照提示来动手破解信件吧！
# 1 列表 letters 尾部追加 '!'
letters.append("!")
# 2 取出列表 letters 中第 7 到 9 个元素（包含 7 和 9）
sublist = letters[6:9]  # 取出第 7 到 9 个元素
# 3 列表 answer 尾部追加 letters 列表里字符 'x' 的次数（需要转换成字符串类型）
answer = []
answer.append(str(letters.count('x')))  # 追加 'x' 的次数
# 4 列表 answer 尾部追加 letters 列表中最后一个元素
answer.append(letters[-1])  # 追加列表的最后一个元素
# 5 将列表 answer 和列表 letters 中最后的三个元素拼接在一起
answer += letters  # 拼接最后三个元素
# 6 打印结果
print(''.join(answer))